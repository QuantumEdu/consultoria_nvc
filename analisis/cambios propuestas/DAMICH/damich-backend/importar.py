"""
Router: /api/importar
Recibe el CSV exportado por el HTML v2.0 y lo persiste en SQLite.
Usa el módulo csv estándar de Python — sin dependencias externas.
"""
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
import csv
import io

from database import get_db
from models import Importacion, Registro

router = APIRouter()

CSV_COLS = [
    "TIPO", "FECHA", "TIENDA", "FOLIO", "CAJERO",
    "VENTAS", "COBRANZA", "INGRESOS", "EGRESOS", "TOTAL", "CREDITO", "DECLARADO", "DIFERENCIA",
    "CATEGORIA_EGRESO", "CONCEPTO", "MONTO", "COMPROBANTE", "PROVEEDOR",
    "ORIGEN", "DESTINO", "RESPONSABLE",
    "PRODUCTO", "CANTIDAD", "TIPO_MOV", "PRECIO", "VALOR",
    "OPERADOR", "URGENCIA",
    "CLIENTE", "DEUDA_ID", "FORMA_PAGO",
    "OBSERVACIONES",
]

TIPOS_VALIDOS = {"CORTE", "EGRESO", "TRASPASO", "KILEADO", "PEDIDO", "DEUDA", "ABONO"}


def _float(val: str) -> float:
    try:
        return float(val.replace(",", "").strip()) if val and val.strip() else 0.0
    except (ValueError, AttributeError):
        return 0.0


def _str(val: str) -> str:
    return val.strip() if val and val.strip() not in ("", "nan") else ""


def _parse_csv(texto: str) -> list[dict]:
    """Parsea el CSV y devuelve lista de dicts, ignorando filas sin tipo válido."""
    reader = csv.DictReader(io.StringIO(texto))

    # Normalizar nombres de columnas (quitar espacios y BOM residual)
    filas = []
    for raw in reader:
        fila = {k.strip().lstrip("\ufeff").upper(): v for k, v in raw.items()}
        tipo = fila.get("TIPO", "").strip().upper()
        if tipo in TIPOS_VALIDOS:
            filas.append(fila)

    return filas


@router.post("/csv", summary="Importar CSV exportado desde el formulario")
def importar_csv(
    archivo: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    if not archivo.filename.lower().endswith(".csv"):
        raise HTTPException(400, "Solo se aceptan archivos .csv")

    contenido = archivo.file.read()

    # Detectar BOM UTF-8
    try:
        texto = contenido.decode("utf-8-sig")
    except UnicodeDecodeError:
        texto = contenido.decode("latin-1")

    try:
        filas = _parse_csv(texto)
    except Exception as e:
        raise HTTPException(400, f"Error al parsear el CSV: {e}")

    if not filas:
        raise HTTPException(400, "El archivo no contiene filas válidas.")

    # Contadores por tipo
    conteo: dict[str, int] = {}
    for f in filas:
        t = f.get("TIPO", "").strip().upper()
        conteo[t] = conteo.get(t, 0) + 1

    # Registro de importación
    imp = Importacion(
        archivo=archivo.filename,
        total_filas=len(filas),
        cortes=conteo.get("CORTE", 0),
        egresos=conteo.get("EGRESO", 0),
        traspasos=conteo.get("TRASPASO", 0),
        kileados=conteo.get("KILEADO", 0),
        pedidos=conteo.get("PEDIDO", 0),
        deudas=conteo.get("DEUDA", 0),
        abonos=conteo.get("ABONO", 0),
    )
    db.add(imp)
    db.flush()

    registros = []
    for row in filas:
        r = Registro(
            importacion_id=imp.id,
            tipo=_str(row.get("TIPO", "")),
            fecha=_str(row.get("FECHA", "")),
            tienda=_str(row.get("TIENDA", "")),
            folio=_str(row.get("FOLIO", "")),
            cajero=_str(row.get("CAJERO", "")),
            ventas=_float(row.get("VENTAS", "")),
            cobranza=_float(row.get("COBRANZA", "")),
            ingresos=_float(row.get("INGRESOS", "")),
            egresos_corte=_float(row.get("EGRESOS", "")),
            total=_float(row.get("TOTAL", "")),
            credito=_float(row.get("CREDITO", "")),
            declarado=_float(row.get("DECLARADO", "")),
            diferencia=_float(row.get("DIFERENCIA", "")),
            categoria_egreso=_str(row.get("CATEGORIA_EGRESO", "")),
            concepto=_str(row.get("CONCEPTO", "")),
            monto=_float(row.get("MONTO", "")),
            comprobante=_str(row.get("COMPROBANTE", "")),
            proveedor=_str(row.get("PROVEEDOR", "")),
            origen=_str(row.get("ORIGEN", "")),
            destino=_str(row.get("DESTINO", "")),
            responsable=_str(row.get("RESPONSABLE", "")),
            producto=_str(row.get("PRODUCTO", "")),
            cantidad=_float(row.get("CANTIDAD", "")),
            tipo_mov=_str(row.get("TIPO_MOV", "")),
            precio=_float(row.get("PRECIO", "")),
            valor=_float(row.get("VALOR", "")),
            operador=_str(row.get("OPERADOR", "")),
            urgencia=_str(row.get("URGENCIA", "")),
            cliente=_str(row.get("CLIENTE", "")),
            deuda_ref_id=_str(row.get("DEUDA_ID", "")),
            forma_pago=_str(row.get("FORMA_PAGO", "")),
            observaciones=_str(row.get("OBSERVACIONES", "")),
        )
        registros.append(r)

    db.bulk_save_objects(registros)
    db.commit()

    return {
        "ok": True,
        "importacion_id": imp.id,
        "archivo": archivo.filename,
        "total_filas": len(filas),
        "detalle": conteo,
    }


@router.get("/historial", summary="Listado de importaciones realizadas")
def historial_importaciones(db: Session = Depends(get_db)):
    imports = db.query(Importacion).order_by(Importacion.id.desc()).limit(50).all()
    return [
        {
            "id": i.id,
            "fecha": str(i.fecha_importacion),
            "archivo": i.archivo,
            "total_filas": i.total_filas,
            "detalle": {
                "cortes": i.cortes, "egresos": i.egresos,
                "traspasos": i.traspasos, "kileados": i.kileados,
                "pedidos": i.pedidos, "deudas": i.deudas, "abonos": i.abonos,
            },
        }
        for i in imports
    ]


@router.delete("/borrar-todo", summary="Eliminar todos los registros (resetear la BD)")
def borrar_todo(db: Session = Depends(get_db)):
    db.execute(text("DELETE FROM registros"))
    db.execute(text("DELETE FROM importaciones"))
    db.commit()
    return {"ok": True, "mensaje": "Base de datos limpiada."}
