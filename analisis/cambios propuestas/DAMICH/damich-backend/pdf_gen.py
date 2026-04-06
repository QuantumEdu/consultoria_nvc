"""
Generador de PDFs con fpdf2.
Usa fuentes estándar — compatible con Windows sin dependencias externas.
Los caracteres especiales del español (á, é, ñ, etc.) están en Latin-1 y funcionan.
"""
from fpdf import FPDF
from datetime import datetime
from typing import Optional


# ─── Colores corporativos DAMICH ──────────────────────────────
AZUL    = (27,  58, 107)
AZUL_C  = (214, 228, 240)
VERDE   = (26, 107,  58)
ROJO    = (180,   0,   0)
NARANJA = (192,  94,   0)
GRIS_BG = (244, 246, 250)
TEXTO_S = (90, 101, 128)


class DamichPDF(FPDF):
    def __init__(self, titulo: str, subtitulo: str = ""):
        super().__init__()
        self.titulo    = titulo
        self.subtitulo = subtitulo
        self.set_auto_page_break(auto=True, margin=18)
        self.add_page()

    def header(self):
        # Banda azul superior
        self.set_fill_color(*AZUL)
        self.rect(0, 0, 210, 18, "F")

        self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 13)
        self.set_y(4)
        self.cell(0, 10, f"DAMICH — {self.titulo}", align="L", padding=(0, 8, 0, 8))

        self.set_font("Helvetica", "", 8)
        self.set_y(4)
        ts = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.cell(0, 10, ts, align="R", padding=(0, 8, 0, 8))

        self.ln(14)
        self.set_text_color(0, 0, 0)

        if self.subtitulo:
            self.set_font("Helvetica", "I", 9)
            self.set_text_color(*TEXTO_S)
            self.cell(0, 6, self.subtitulo, ln=True)
            self.ln(2)
            self.set_text_color(0, 0, 0)

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(*TEXTO_S)
        self.cell(0, 6, f"Página {self.page_no()}", align="C")

    def seccion(self, texto: str):
        """Encabezado de sección con fondo azul claro."""
        self.set_fill_color(*AZUL_C)
        self.set_text_color(*AZUL)
        self.set_font("Helvetica", "B", 9)
        self.cell(0, 7, f"  {texto}", ln=True, fill=True)
        self.set_text_color(0, 0, 0)
        self.ln(1)

    def kpi_row(self, items: list[tuple[str, str]]):
        """Fila de KPIs: lista de (label, valor)."""
        ancho = (self.w - 2 * self.l_margin) / len(items)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*TEXTO_S)
        for label, _ in items:
            self.cell(ancho, 5, label, align="C")
        self.ln()
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(*AZUL)
        for _, valor in items:
            self.cell(ancho, 8, valor, align="C")
        self.ln(10)
        self.set_text_color(0, 0, 0)

    def tabla(
        self,
        columnas: list[str],
        anchos: list[int],
        filas: list[list],
        alinear: Optional[list[str]] = None,
    ):
        """Tabla genérica con cabecera azul y filas alternadas."""
        alinear = alinear or ["L"] * len(columnas)

        # Cabecera
        self.set_fill_color(*AZUL)
        self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 8)
        for col, ancho, ali in zip(columnas, anchos, alinear):
            self.cell(ancho, 7, col, border=0, fill=True, align=ali)
        self.ln()

        # Filas
        self.set_text_color(0, 0, 0)
        self.set_font("Helvetica", "", 8)
        par = False
        for fila in filas:
            if self.get_y() > self.h - 25:
                self.add_page()
            self.set_fill_color(*(GRIS_BG if par else (255, 255, 255)))
            for celda, ancho, ali in zip(fila, anchos, alinear):
                self.cell(ancho, 6, str(celda or ""), fill=True, align=ali)
            self.ln()
            par = not par

        self.ln(3)


def fmt_mxn(valor) -> str:
    try:
        return f"${float(valor):,.2f}"
    except (TypeError, ValueError):
        return "$0.00"


# ─────────────────────────────────────────────────────────────────────
# PDF: DASHBOARD
# ─────────────────────────────────────────────────────────────────────

def pdf_dashboard(data: dict, filtro_desc: str = "") -> bytes:
    pdf = DamichPDF("Resumen Ejecutivo", subtitulo=filtro_desc or "Todos los períodos")

    # KPIs principales
    pdf.seccion("Ventas e Ingresos")
    pdf.kpi_row([
        ("Ventas Totales",    fmt_mxn(data.get("ventas_totales", 0))),
        ("Ingresos Totales",  fmt_mxn(data.get("ingresos_totales", 0))),
        ("Cobranza",          fmt_mxn(data.get("cobranza_total", 0))),
        ("Crédito",           fmt_mxn(data.get("credito_total", 0))),
    ])

    pdf.seccion("Egresos y Deudas")
    pdf.kpi_row([
        ("Egresos en Corte",  fmt_mxn(data.get("egresos_en_corte", 0))),
        ("Egresos Registrados", fmt_mxn(data.get("egresos_registrados", 0))),
        ("Saldo Deudas",      fmt_mxn(data.get("saldo_deudas", 0))),
        ("Mejor Día",         str(data.get("mejor_dia_semana") or "N/D")),
    ])

    # Ventas por sucursal
    pdf.seccion("Ventas por Sucursal")
    ventas_x = data.get("ventas_x_sucursal", [])
    pdf.tabla(
        columnas=["Sucursal", "Ventas Totales"],
        anchos=[120, 70],
        filas=[[r["tienda"], fmt_mxn(r["ventas"])] for r in ventas_x],
        alinear=["L", "R"],
    )

    # Ventas por día de semana
    pdf.seccion("Ventas por Día de Semana")
    ventas_dia = data.get("ventas_x_dia_semana", {})
    orden_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    filas_dia = [
        [dia, fmt_mxn(ventas_dia.get(dia, 0))]
        for dia in orden_dias
        if dia in ventas_dia
    ]
    pdf.tabla(
        columnas=["Día", "Ventas Acumuladas"],
        anchos=[90, 100],
        filas=filas_dia,
        alinear=["L", "R"],
    )

    return bytes(pdf.output())


# ─────────────────────────────────────────────────────────────────────
# PDF: CORTES DE CAJA
# ─────────────────────────────────────────────────────────────────────

def pdf_cortes(data: dict, filtro_desc: str = "") -> bytes:
    pdf = DamichPDF("Cortes de Caja", subtitulo=filtro_desc)

    tot = data.get("totales", {})
    pdf.seccion("Totales del período")
    pdf.kpi_row([
        ("Ingresos",   fmt_mxn(tot.get("ingresos", 0))),
        ("Egresos",    fmt_mxn(tot.get("egresos", 0))),
        ("Declarado",  fmt_mxn(tot.get("declarado", 0))),
        ("Diferencia", fmt_mxn(tot.get("diferencia", 0))),
    ])

    pdf.seccion("Detalle de Cortes")
    pdf.tabla(
        columnas=["Fecha", "Tienda", "Folio", "Ventas", "Cobranza", "Egresos", "Declarado", "Diferencia"],
        anchos=[22, 38, 18, 24, 22, 20, 24, 22],
        filas=[
            [
                r["fecha"], r["tienda"], r["folio"],
                fmt_mxn(r["ventas"]), fmt_mxn(r["cobranza"]),
                fmt_mxn(r["egresos"]), fmt_mxn(r["declarado"]),
                fmt_mxn(r["diferencia"]),
            ]
            for r in data.get("registros", [])
        ],
        alinear=["L", "L", "C", "R", "R", "R", "R", "R"],
    )

    return bytes(pdf.output())


# ─────────────────────────────────────────────────────────────────────
# PDF: EGRESOS
# ─────────────────────────────────────────────────────────────────────

def pdf_egresos(data: dict, filtro_desc: str = "") -> bytes:
    pdf = DamichPDF("Egresos", subtitulo=filtro_desc)

    pdf.seccion("Resumen")
    pdf.kpi_row([
        ("Total Egresos", fmt_mxn(data.get("total", 0))),
        ("N° Registros",  str(data.get("n", 0))),
    ])

    pdf.seccion("Por Categoría")
    pdf.tabla(
        columnas=["Categoría", "Total"],
        anchos=[140, 50],
        filas=[[r["categoria"], fmt_mxn(r["total"])] for r in data.get("por_categoria", [])],
        alinear=["L", "R"],
    )

    pdf.seccion("Detalle")
    pdf.tabla(
        columnas=["Fecha", "Tienda", "Categoría", "Concepto", "Monto"],
        anchos=[22, 35, 35, 68, 30],
        filas=[
            [r["fecha"], r["tienda"], r["categoria"], r["concepto"], fmt_mxn(r["monto"])]
            for r in data.get("registros", [])
        ],
        alinear=["L", "L", "L", "L", "R"],
    )

    return bytes(pdf.output())


# ─────────────────────────────────────────────────────────────────────
# PDF: DEUDAS
# ─────────────────────────────────────────────────────────────────────

def pdf_deudas(data: dict, filtro_desc: str = "") -> bytes:
    pdf = DamichPDF("Deudas y Cobranza", subtitulo=filtro_desc)

    pdf.seccion("Resumen")
    pdf.kpi_row([
        ("Total Adeudado",   fmt_mxn(data.get("total_adeudado", 0))),
        ("Total Abonado",    fmt_mxn(data.get("total_abonado", 0))),
        ("Saldo Pendiente",  fmt_mxn(data.get("saldo_pendiente", 0))),
        ("N° Deudas",        str(data.get("n_deudas", 0))),
    ])

    pdf.seccion("Detalle de Deudas")
    pdf.tabla(
        columnas=["Fecha", "Tienda", "Cliente", "Concepto", "Total", "Abonado", "Saldo", "Estado"],
        anchos=[20, 28, 32, 38, 22, 20, 20, 10],
        filas=[
            [
                r["fecha"], r["tienda"], r["cliente"], r["concepto"],
                fmt_mxn(r["monto_total"]), fmt_mxn(r["abonado"]),
                fmt_mxn(r["saldo"]), r["estado"][0].upper(),
            ]
            for r in data.get("deudas", [])
        ],
        alinear=["L", "L", "L", "L", "R", "R", "R", "C"],
    )

    return bytes(pdf.output())


# ─────────────────────────────────────────────────────────────────────
# PDF: TOP PRODUCTOS
# ─────────────────────────────────────────────────────────────────────

def pdf_productos_top(data: dict, filtro_desc: str = "") -> bytes:
    pdf = DamichPDF("Top Productos", subtitulo=filtro_desc)

    pdf.seccion(f"Ranking de movimiento ({data.get('n_productos', 0)} productos)")
    pdf.tabla(
        columnas=["#", "Producto", "Cant. Kileado", "Valor Kileado", "Cant. Traspaso", "Total Movido"],
        anchos=[8, 70, 25, 30, 27, 30],
        filas=[
            [
                str(i + 1),
                r["producto"],
                str(round(r["cant_kileado"], 1)),
                fmt_mxn(r["valor_kileado"]),
                str(round(r["cant_traspaso"], 1)),
                str(round(r["movimiento_total"], 1)),
            ]
            for i, r in enumerate(data.get("productos", []))
        ],
        alinear=["C", "L", "R", "R", "R", "R"],
    )

    return bytes(pdf.output())
