from sqlalchemy import Column, Integer, Float, ForeignKey,Computed
from sqlalchemy.orm import relationship
from app.models.database import Base

class DetalleVenta(Base):
    __tablename__ = "detalle_ventas"

    id = Column(Integer, primary_key=True, index=True)
    venta_id = Column(Integer, ForeignKey("ventas.id", ondelete="CASCADE"), nullable=False)
    producto_id = Column(Integer, ForeignKey("productos.id", ondelete="CASCADE"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)

    # Usar Computed para permitir que la base de datos calcule el subtotal
    subtotal = Column(Float, Computed("cantidad * precio_unitario"), nullable=False)
    #subtotal = Column(Float, nullable=False)

    # Relación inversa con el modelo Venta
    venta = relationship("Venta", back_populates="detalles")
