"""
DAMICH Backend — v1.0
FastAPI + SQLite
Corre en: python main.py  (o: uvicorn main:app --reload)
Docs:     http://localhost:8000/docs
"""
from fastapi import FastAPI, Depends, Query, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import Optional
import os

from database import engine, Base, get_db
import importar
import reportes
from pdf_gen import (
    pdf_dashboard,
    pdf_cortes,
    pdf_egresos,
    pdf_deudas,
    pdf_productos_top,
)

# ── Crear tablas al arrancar ──────────────────────────────────────────
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DAMICH Backend",
    description="API para importar CSVs del formulario de captura y generar reportes.",
    version="1.0.0",
)

# CORS abierto: el HTML se sirve como archivo local (file://)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(importar.router, prefix="/api/importar", tags=["Importar CSV"])
app.include_router(reportes.router, prefix="/api/reportes", tags=["Reportes"])


# ─────────────────────────────────────────────────────────────────────
# PDF ENDPOINTS — devuelven application/pdf directamente
# ─────────────────────────────────────────────────────────────────────

def _filtro_desc(tienda, fecha_inicio, fecha_fin, mes):
    partes = []
    if tienda:       partes.append(tienda)
    if mes:          partes.append(f"Mes: {mes}")
    elif fecha_inicio or fecha_fin:
        partes.append(f"{fecha_inicio or '...'} → {fecha_fin or '...'}")
    return " | ".join(partes) if partes else "Todos los datos"


@app.get("/api/pdf/dashboard", tags=["PDF"], summary="PDF del resumen ejecutivo")
def pdf_rpt_dashboard(
    tienda:       Optional[str] = Query(None),
    fecha_inicio: Optional[str] = Query(None),
    fecha_fin:    Optional[str] = Query(None),
    mes:          Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    filtros = {"tienda": tienda, "fecha_inicio": fecha_inicio, "fecha_fin": fecha_fin, "mes": mes}
    from reportes import dashboard as _dashboard
    data = _dashboard(filtros=filtros, db=db)
    contenido = pdf_dashboard(data, _filtro_desc(tienda, fecha_inicio, fecha_fin, mes))
    return Response(content=contenido, media_type="application/pdf",
                    headers={"Content-Disposition": "inline; filename=dashboard.pdf"})


@app.get("/api/pdf/cortes", tags=["PDF"], summary="PDF de cortes de caja")
def pdf_rpt_cortes(
    tienda:       Optional[str] = Query(None),
    fecha_inicio: Optional[str] = Query(None),
    fecha_fin:    Optional[str] = Query(None),
    mes:          Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    filtros = {"tienda": tienda, "fecha_inicio": fecha_inicio, "fecha_fin": fecha_fin, "mes": mes}
    from reportes import reporte_cortes as _cortes
    data = _cortes(filtros=filtros, db=db)
    contenido = pdf_cortes(data, _filtro_desc(tienda, fecha_inicio, fecha_fin, mes))
    return Response(content=contenido, media_type="application/pdf",
                    headers={"Content-Disposition": "inline; filename=cortes.pdf"})


@app.get("/api/pdf/egresos", tags=["PDF"], summary="PDF de egresos con desglose por categoría")
def pdf_rpt_egresos(
    tienda:       Optional[str] = Query(None),
    fecha_inicio: Optional[str] = Query(None),
    fecha_fin:    Optional[str] = Query(None),
    mes:          Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    filtros = {"tienda": tienda, "fecha_inicio": fecha_inicio, "fecha_fin": fecha_fin, "mes": mes}
    from reportes import reporte_egresos as _egresos
    data = _egresos(filtros=filtros, db=db)
    contenido = pdf_egresos(data, _filtro_desc(tienda, fecha_inicio, fecha_fin, mes))
    return Response(content=contenido, media_type="application/pdf",
                    headers={"Content-Disposition": "inline; filename=egresos.pdf"})


@app.get("/api/pdf/deudas", tags=["PDF"], summary="PDF del estado de deudas y cobranza")
def pdf_rpt_deudas(
    tienda:   Optional[str] = Query(None),
    cliente:  Optional[str] = Query(None),
    estado:   Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    from reportes import reporte_deudas as _deudas
    filtros = {"tienda": tienda, "fecha_inicio": None, "fecha_fin": None, "mes": None}
    data = _deudas(filtros=filtros, cliente=cliente, estado=estado, db=db)
    contenido = pdf_deudas(data, tienda or "Todas las sucursales")
    return Response(content=contenido, media_type="application/pdf",
                    headers={"Content-Disposition": "inline; filename=deudas.pdf"})


@app.get("/api/pdf/productos-top", tags=["PDF"], summary="PDF del ranking de productos")
def pdf_rpt_productos(
    tienda:       Optional[str] = Query(None),
    fecha_inicio: Optional[str] = Query(None),
    fecha_fin:    Optional[str] = Query(None),
    mes:          Optional[str] = Query(None),
    limite:       int           = Query(30),
    db: Session = Depends(get_db),
):
    filtros = {"tienda": tienda, "fecha_inicio": fecha_inicio, "fecha_fin": fecha_fin, "mes": mes}
    from reportes import productos_top as _top
    data = _top(filtros=filtros, limite=limite, db=db)
    contenido = pdf_productos_top(data, _filtro_desc(tienda, fecha_inicio, fecha_fin, mes))
    return Response(content=contenido, media_type="application/pdf",
                    headers={"Content-Disposition": "inline; filename=productos_top.pdf"})


# ─────────────────────────────────────────────────────────────────────
# ROOT
# ─────────────────────────────────────────────────────────────────────

@app.get("/dashboard", tags=["Info"], include_in_schema=False)
def serve_dashboard():
    path = os.path.join(os.path.dirname(__file__), "dashboard.html")
    return FileResponse(path, media_type="text/html")


@app.get("/", tags=["Info"])
def root():
    return {
        "sistema": "DAMICH Backend",
        "version": "1.0.0",
        "docs":    "/docs",
        "endpoints": {
            "importar_csv":   "POST /api/importar/csv",
            "historial":      "GET  /api/importar/historial",
            "dashboard":      "GET  /api/reportes/dashboard",
            "cortes":         "GET  /api/reportes/cortes",
            "egresos":        "GET  /api/reportes/egresos",
            "traspasos":      "GET  /api/reportes/traspasos",
            "kileados":       "GET  /api/reportes/kileados",
            "pedidos":        "GET  /api/reportes/pedidos",
            "deudas":         "GET  /api/reportes/deudas",
            "productos_top":  "GET  /api/reportes/productos-top",
            "pdf_dashboard":  "GET  /api/pdf/dashboard",
            "pdf_cortes":     "GET  /api/pdf/cortes",
            "pdf_egresos":    "GET  /api/pdf/egresos",
            "pdf_deudas":     "GET  /api/pdf/deudas",
            "pdf_productos":  "GET  /api/pdf/productos-top",
        },
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
