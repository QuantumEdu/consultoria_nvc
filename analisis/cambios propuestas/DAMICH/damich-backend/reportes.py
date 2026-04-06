"""
Router: /api/reportes
Genera reportes filtrados desde la BD SQLite.
Todos los endpoints aceptan los mismos query params opcionales:
  tienda, fecha_inicio, fecha_fin, mes (YYYY-MM)
"""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func, case
from typing import Optional
from datetime import datetime

from database import get_db
from models import Registro

router = APIRouter()


# ─────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────

def aplicar_filtros(
    query,
    tipo: str,
    tienda: Optional[str],
    fecha_inicio: Optional[str],
    fecha_fin: Optional[str],
    mes: Optional[str],
):
    """Aplica filtros comunes a una consulta SQLAlchemy."""
    query = query.filter(Registro.tipo == tipo)
    if tienda:
        query = query.filter(Registro.tienda == tienda)
    if mes:                                     # YYYY-MM → rango del mes
        fecha_inicio = fecha_inicio or f"{mes}-01"
        fecha_fin    = fecha_fin    or f"{mes}-31"
    if fecha_inicio:
        query = query.filter(Registro.fecha >= fecha_inicio)
    if fecha_fin:
        query = query.filter(Registro.fecha <= fecha_fin)
    return query


def filtros_comunes(
    tienda:       Optional[str] = Query(None, description="APATZINGÁN | NUEVA ITALIA | SAN SIMÓN"),
    fecha_inicio: Optional[str] = Query(None, description="YYYY-MM-DD"),
    fecha_fin:    Optional[str] = Query(None, description="YYYY-MM-DD"),
    mes:          Optional[str] = Query(None, description="YYYY-MM — atajo para filtrar un mes completo"),
):
    return {"tienda": tienda, "fecha_inicio": fecha_inicio, "fecha_fin": fecha_fin, "mes": mes}


# ─────────────────────────────────────────────────────────
# DASHBOARD — resumen ejecutivo
# ─────────────────────────────────────────────────────────

@router.get("/dashboard", summary="Resumen general de KPIs")
def dashboard(
    filtros: dict = Depends(filtros_comunes),
    db: Session = Depends(get_db),
):
    tienda       = filtros["tienda"]
    fecha_inicio = filtros["fecha_inicio"]
    fecha_fin    = filtros["fecha_fin"]
    mes          = filtros["mes"]

    def _fi(tipo: str):
        return aplicar_filtros(
            db.query(Registro), tipo, tienda, fecha_inicio, fecha_fin, mes
        )

    # Cortes
    cortes = _fi("CORTE").with_entities(
        func.sum(Registro.ventas).label("ventas"),
        func.sum(Registro.cobranza).label("cobranza"),
        func.sum(Registro.ingresos).label("ingresos"),
        func.sum(Registro.egresos_corte).label("egresos_corte"),
        func.sum(Registro.credito).label("credito"),
        func.count().label("n"),
    ).first()

    # Egresos explícitos
    egresos = _fi("EGRESO").with_entities(
        func.sum(Registro.monto).label("total"),
        func.count().label("n"),
    ).first()

    # Kileados — valor total
    kileados = _fi("KILEADO").with_entities(
        func.sum(Registro.valor).label("total"),
        func.count().label("n"),
    ).first()

    # Deudas pendientes (todas las deudas sin filtro de tienda/fecha para mostrar saldo real)
    total_deudas = db.query(func.sum(Registro.monto)).filter(Registro.tipo == "DEUDA").scalar() or 0
    total_abonos = db.query(func.sum(Registro.monto)).filter(Registro.tipo == "ABONO").scalar() or 0
    saldo_deudas = total_deudas - total_abonos

    # Ventas por día de semana (últimos registros de corte)
    cortes_todos = _fi("CORTE").with_entities(Registro.fecha, Registro.ventas).all()
    ventas_x_dia = {}
    dias_es = {0: "Lunes", 1: "Martes", 2: "Miércoles", 3: "Jueves", 4: "Viernes", 5: "Sábado", 6: "Domingo"}
    for row in cortes_todos:
        try:
            dia = datetime.strptime(row.fecha, "%Y-%m-%d").weekday()
            nombre = dias_es[dia]
            ventas_x_dia[nombre] = ventas_x_dia.get(nombre, 0) + (row.ventas or 0)
        except Exception:
            pass

    mejor_dia = max(ventas_x_dia, key=ventas_x_dia.get) if ventas_x_dia else None

    # Ventas por sucursal
    ventas_x_tienda = (
        db.query(Registro.tienda, func.sum(Registro.ventas).label("total"))
        .filter(Registro.tipo == "CORTE")
        .group_by(Registro.tienda)
        .all()
    )

    return {
        "ventas_totales":    round(cortes.ventas or 0, 2),
        "cobranza_total":    round(cortes.cobranza or 0, 2),
        "ingresos_totales":  round(cortes.ingresos or 0, 2),
        "egresos_en_corte":  round(cortes.egresos_corte or 0, 2),
        "credito_total":     round(cortes.credito or 0, 2),
        "n_cortes":          cortes.n or 0,
        "egresos_registrados": round(egresos.total or 0, 2),
        "n_egresos":         egresos.n or 0,
        "valor_kileado":     round(kileados.total or 0, 2),
        "n_kileados":        kileados.n or 0,
        "saldo_deudas":      round(saldo_deudas, 2),
        "mejor_dia_semana":  mejor_dia,
        "ventas_x_dia_semana": ventas_x_dia,
        "ventas_x_sucursal": [
            {"tienda": r.tienda, "ventas": round(r.total or 0, 2)}
            for r in ventas_x_tienda
        ],
    }


# ─────────────────────────────────────────────────────────
# CORTES DE CAJA
# ─────────────────────────────────────────────────────────

@router.get("/cortes", summary="Cortes de caja filtrados")
def reporte_cortes(
    filtros: dict = Depends(filtros_comunes),
    db: Session = Depends(get_db),
):
    q = aplicar_filtros(
        db.query(Registro), "CORTE",
        filtros["tienda"], filtros["fecha_inicio"], filtros["fecha_fin"], filtros["mes"]
    ).order_by(Registro.fecha.desc())

    rows = q.all()
    totales = {
        "ventas":     round(sum(r.ventas    or 0 for r in rows), 2),
        "cobranza":   round(sum(r.cobranza  or 0 for r in rows), 2),
        "ingresos":   round(sum(r.ingresos  or 0 for r in rows), 2),
        "egresos":    round(sum(r.egresos_corte or 0 for r in rows), 2),
        "declarado":  round(sum(r.declarado or 0 for r in rows), 2),
        "diferencia": round(sum(r.diferencia or 0 for r in rows), 2),
        "n": len(rows),
    }

    return {
        "totales": totales,
        "registros": [
            {
                "fecha":      r.fecha,
                "tienda":     r.tienda,
                "folio":      r.folio,
                "cajero":     r.cajero,
                "ventas":     r.ventas,
                "cobranza":   r.cobranza,
                "ingresos":   r.ingresos,
                "egresos":    r.egresos_corte,
                "declarado":  r.declarado,
                "diferencia": r.diferencia,
                "obs":        r.observaciones,
            }
            for r in rows
        ],
    }


# ─────────────────────────────────────────────────────────
# EGRESOS
# ─────────────────────────────────────────────────────────

@router.get("/egresos", summary="Egresos registrados con desglose por categoría")
def reporte_egresos(
    filtros: dict = Depends(filtros_comunes),
    db: Session = Depends(get_db),
):
    q = aplicar_filtros(
        db.query(Registro), "EGRESO",
        filtros["tienda"], filtros["fecha_inicio"], filtros["fecha_fin"], filtros["mes"]
    ).order_by(Registro.fecha.desc())

    rows = q.all()

    # Desglose por categoría
    x_categoria: dict = {}
    for r in rows:
        cat = r.categoria_egreso or "SIN CATEGORÍA"
        x_categoria[cat] = x_categoria.get(cat, 0) + (r.monto or 0)

    return {
        "total": round(sum(r.monto or 0 for r in rows), 2),
        "n": len(rows),
        "por_categoria": [
            {"categoria": k, "total": round(v, 2)}
            for k, v in sorted(x_categoria.items(), key=lambda x: -x[1])
        ],
        "registros": [
            {
                "fecha":      r.fecha,
                "tienda":     r.tienda,
                "categoria":  r.categoria_egreso,
                "concepto":   r.concepto,
                "monto":      r.monto,
                "comprobante": r.comprobante,
                "proveedor":  r.proveedor,
                "obs":        r.observaciones,
            }
            for r in rows
        ],
    }


# ─────────────────────────────────────────────────────────
# TRASPASOS
# ─────────────────────────────────────────────────────────

@router.get("/traspasos", summary="Traspasos entre sucursales")
def reporte_traspasos(
    origen:  Optional[str] = Query(None),
    destino: Optional[str] = Query(None),
    filtros: dict = Depends(filtros_comunes),
    db: Session = Depends(get_db),
):
    q = db.query(Registro).filter(Registro.tipo == "TRASPASO")
    if origen:
        q = q.filter(Registro.origen == origen)
    if destino:
        q = q.filter(Registro.destino == destino)
    if filtros["mes"]:
        filtros["fecha_inicio"] = filtros["fecha_inicio"] or f"{filtros['mes']}-01"
        filtros["fecha_fin"]    = filtros["fecha_fin"]    or f"{filtros['mes']}-31"
    if filtros["fecha_inicio"]:
        q = q.filter(Registro.fecha >= filtros["fecha_inicio"])
    if filtros["fecha_fin"]:
        q = q.filter(Registro.fecha <= filtros["fecha_fin"])
    q = q.order_by(Registro.fecha.desc(), Registro.folio)

    rows = q.all()

    # Agrupar por (fecha, folio, origen, destino) para reconstruir traspasos
    grupos: dict = {}
    for r in rows:
        key = (r.fecha, r.folio, r.origen, r.destino)
        if key not in grupos:
            grupos[key] = {
                "fecha": r.fecha, "folio": r.folio,
                "origen": r.origen, "destino": r.destino,
                "responsable": r.responsable,
                "obs": r.observaciones,
                "productos": [],
            }
        if r.producto:
            grupos[key]["productos"].append({
                "producto": r.producto,
                "cantidad": r.cantidad,
                "unidad": r.tipo_mov,
            })

    return {
        "n_traspasos": len(grupos),
        "n_productos": len(rows),
        "traspasos": list(grupos.values()),
    }


# ─────────────────────────────────────────────────────────
# KILEADOS
# ─────────────────────────────────────────────────────────

@router.get("/kileados", summary="Registros de kileado / suelto")
def reporte_kileados(
    operador: Optional[str] = Query(None),
    tipo_mov: Optional[str] = Query(None, description="K o S"),
    filtros:  dict = Depends(filtros_comunes),
    db: Session = Depends(get_db),
):
    q = aplicar_filtros(
        db.query(Registro), "KILEADO",
        filtros["tienda"], filtros["fecha_inicio"], filtros["fecha_fin"], filtros["mes"]
    )
    if operador:
        q = q.filter(Registro.operador == operador)
    if tipo_mov:
        q = q.filter(Registro.tipo_mov == tipo_mov.upper())

    rows = q.order_by(Registro.fecha.desc()).all()

    # Top productos por cantidad
    top: dict = {}
    for r in rows:
        if r.producto:
            if r.producto not in top:
                top[r.producto] = {"cantidad": 0, "valor": 0, "veces": 0}
            top[r.producto]["cantidad"] += r.cantidad or 0
            top[r.producto]["valor"]    += r.valor    or 0
            top[r.producto]["veces"]    += 1

    top_sorted = sorted(top.items(), key=lambda x: -x[1]["cantidad"])

    return {
        "total_valor": round(sum(r.valor or 0 for r in rows), 2),
        "n": len(rows),
        "top_productos": [
            {"producto": k, **v} for k, v in top_sorted[:20]
        ],
        "registros": [
            {
                "fecha":    r.fecha,
                "tienda":   r.tienda,
                "operador": r.operador,
                "producto": r.producto,
                "cantidad": r.cantidad,
                "tipo":     r.tipo_mov,
                "precio":   r.precio,
                "valor":    r.valor,
                "obs":      r.observaciones,
            }
            for r in rows
        ],
    }


# ─────────────────────────────────────────────────────────
# PEDIDOS
# ─────────────────────────────────────────────────────────

@router.get("/pedidos", summary="Pedidos registrados")
def reporte_pedidos(
    urgencia: Optional[str] = Query(None),
    filtros:  dict = Depends(filtros_comunes),
    db: Session = Depends(get_db),
):
    q = aplicar_filtros(
        db.query(Registro), "PEDIDO",
        filtros["tienda"], filtros["fecha_inicio"], filtros["fecha_fin"], filtros["mes"]
    )
    if urgencia:
        q = q.filter(Registro.urgencia == urgencia.upper())

    rows = q.order_by(Registro.fecha.desc()).all()

    # Agrupar por (fecha, tienda, obs) → reconstruir pedidos
    grupos: dict = {}
    for r in rows:
        key = (r.fecha, r.tienda, r.observaciones or "")
        if key not in grupos:
            grupos[key] = {
                "fecha": r.fecha, "tienda": r.tienda,
                "urgencia": r.urgencia, "obs": r.observaciones,
                "productos": [],
            }
        if r.producto:
            grupos[key]["productos"].append({
                "producto": r.producto,
                "cantidad": r.cantidad,
                "unidad": r.tipo_mov,
            })

    return {
        "n_pedidos": len(grupos),
        "pedidos": list(grupos.values()),
    }


# ─────────────────────────────────────────────────────────
# DEUDAS Y COBRANZA
# ─────────────────────────────────────────────────────────

@router.get("/deudas", summary="Estado de deudas y cobranza por cliente")
def reporte_deudas(
    cliente:  Optional[str] = Query(None),
    estado:   Optional[str] = Query(None, description="abierta | cerrada | todas"),
    filtros:  dict = Depends(filtros_comunes),
    db: Session = Depends(get_db),
):
    q_deudas = db.query(Registro).filter(Registro.tipo == "DEUDA")
    if filtros["tienda"]:
        q_deudas = q_deudas.filter(Registro.tienda == filtros["tienda"])
    if cliente:
        q_deudas = q_deudas.filter(Registro.cliente.ilike(f"%{cliente}%"))

    deudas = q_deudas.order_by(Registro.fecha.desc()).all()

    # Calcular abonos por deuda_ref_id
    abonos_q = db.query(
        Registro.deuda_ref_id,
        func.sum(Registro.monto).label("total_abonado"),
    ).filter(Registro.tipo == "ABONO").group_by(Registro.deuda_ref_id).all()

    abonos_map = {a.deuda_ref_id: a.total_abonado or 0 for a in abonos_q}

    # También considerar abonos donde el deuda_ref_id es el ID de BD
    # (el HTML exporta el timestamp JS como deuda_ref_id)

    resultado = []
    for d in deudas:
        # Intentar match por deuda_ref_id (ID original del HTML)
        abonado = abonos_map.get(str(d.deuda_ref_id), 0)
        saldo   = max(0, (d.monto or 0) - abonado)
        est     = "cerrada" if saldo < 0.01 else "abierta"

        if estado and estado != "todas" and est != estado:
            continue

        resultado.append({
            "id_bd":      d.id,
            "fecha":      d.fecha,
            "tienda":     d.tienda,
            "cliente":    d.cliente,
            "concepto":   d.concepto,
            "monto_total": d.monto,
            "abonado":    round(abonado, 2),
            "saldo":      round(saldo, 2),
            "estado":     est,
            "obs":        d.observaciones,
        })

    total_saldo = round(sum(r["saldo"] for r in resultado), 2)
    total_deuda = round(sum(r["monto_total"] for r in resultado), 2)

    return {
        "total_adeudado": total_deuda,
        "total_abonado":  round(total_deuda - total_saldo, 2),
        "saldo_pendiente": total_saldo,
        "n_deudas":       len(resultado),
        "deudas":         resultado,
    }


# ─────────────────────────────────────────────────────────
# PRODUCTOS — ranking global
# ─────────────────────────────────────────────────────────

@router.get("/productos-top", summary="Ranking de productos más movidos (kileado + traspasos)")
def productos_top(
    limite: int = Query(20, ge=1, le=100),
    filtros: dict = Depends(filtros_comunes),
    db: Session = Depends(get_db),
):
    # Kileados: agrupar por producto
    q_k = db.query(
        Registro.producto,
        func.sum(Registro.cantidad).label("cant_kileado"),
        func.sum(Registro.valor).label("valor_kileado"),
    ).filter(
        Registro.tipo == "KILEADO",
        Registro.producto != "",
        Registro.producto != None,
    )
    if filtros["tienda"]:
        q_k = q_k.filter(Registro.tienda == filtros["tienda"])
    if filtros["mes"]:
        filtros["fecha_inicio"] = filtros["fecha_inicio"] or f"{filtros['mes']}-01"
        filtros["fecha_fin"]    = filtros["fecha_fin"]    or f"{filtros['mes']}-31"
    if filtros["fecha_inicio"]:
        q_k = q_k.filter(Registro.fecha >= filtros["fecha_inicio"])
    if filtros["fecha_fin"]:
        q_k = q_k.filter(Registro.fecha <= filtros["fecha_fin"])
    q_k = q_k.group_by(Registro.producto).all()

    # Traspasos: agrupar por producto
    q_t = db.query(
        Registro.producto,
        func.sum(Registro.cantidad).label("cant_traspaso"),
    ).filter(
        Registro.tipo == "TRASPASO",
        Registro.producto != "",
        Registro.producto != None,
    ).group_by(Registro.producto).all()

    mapa_k = {r.producto.upper(): {"cant_k": r.cant_kileado or 0, "valor_k": r.valor_kileado or 0} for r in q_k}
    mapa_t = {r.producto.upper(): r.cant_traspaso or 0 for r in q_t}

    productos_todos = set(mapa_k.keys()) | set(mapa_t.keys())

    ranking = sorted(
        [
            {
                "producto":       p,
                "cant_kileado":   round(mapa_k.get(p, {}).get("cant_k", 0), 2),
                "valor_kileado":  round(mapa_k.get(p, {}).get("valor_k", 0), 2),
                "cant_traspaso":  round(mapa_t.get(p, 0), 2),
                "movimiento_total": round(
                    mapa_k.get(p, {}).get("cant_k", 0) + mapa_t.get(p, 0), 2
                ),
            }
            for p in productos_todos
        ],
        key=lambda x: -x["movimiento_total"],
    )

    return {"n_productos": len(ranking), "productos": ranking[:limite]}
