from sqlalchemy import Column, Integer, Float, String, DateTime, func
from database import Base


class Importacion(Base):
    """Registro de cada CSV importado al sistema."""
    __tablename__ = "importaciones"

    id              = Column(Integer, primary_key=True, index=True)
    fecha_importacion = Column(DateTime, default=func.now())
    archivo         = Column(String)
    total_filas     = Column(Integer)
    cortes          = Column(Integer, default=0)
    egresos         = Column(Integer, default=0)
    traspasos       = Column(Integer, default=0)
    kileados        = Column(Integer, default=0)
    pedidos         = Column(Integer, default=0)
    deudas          = Column(Integer, default=0)
    abonos          = Column(Integer, default=0)


class Registro(Base):
    """
    Tabla plana que refleja las columnas del CSV exportado por el HTML v2.0.
    Un row por línea del CSV — las filas de un mismo traspaso/kileado/pedido
    comparten folio/operador/fecha y se agrupan en los reportes.
    """
    __tablename__ = "registros"

    id              = Column(Integer, primary_key=True, index=True)
    importacion_id  = Column(Integer, index=True)

    # Identificación
    tipo            = Column(String, index=True)   # CORTE|EGRESO|TRASPASO|KILEADO|PEDIDO|DEUDA|ABONO
    fecha           = Column(String, index=True)   # YYYY-MM-DD
    tienda          = Column(String, index=True)

    # Corte de caja
    folio           = Column(String)
    cajero          = Column(String)
    ventas          = Column(Float, default=0)
    cobranza        = Column(Float, default=0)
    ingresos        = Column(Float, default=0)
    egresos_corte   = Column(Float, default=0)    # columna EGRESOS del CSV
    total           = Column(Float, default=0)
    credito         = Column(Float, default=0)
    declarado       = Column(Float, default=0)
    diferencia      = Column(Float, default=0)

    # Egreso
    categoria_egreso = Column(String)
    concepto        = Column(String)
    monto           = Column(Float, default=0)
    comprobante     = Column(String)
    proveedor       = Column(String)

    # Traspaso
    origen          = Column(String)
    destino         = Column(String)
    responsable     = Column(String)

    # Producto (kileado / traspaso / pedido — una fila por producto)
    producto        = Column(String)
    cantidad        = Column(Float, default=0)
    tipo_mov        = Column(String)   # K/S para kileado, unidad para traspaso/pedido
    precio          = Column(Float, default=0)
    valor           = Column(Float, default=0)
    operador        = Column(String)
    urgencia        = Column(String)

    # Deuda / Abono
    cliente         = Column(String, index=True)
    deuda_ref_id    = Column(String)   # ID original de la deuda (desde el HTML)
    forma_pago      = Column(String)

    observaciones   = Column(String)
