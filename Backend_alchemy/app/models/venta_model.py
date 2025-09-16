from sqlalchemy import Column, Integer, Float, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship
from app.models.database import Base

class Venta(Base):
    __tablename__ = "ventas"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)  # Se relaciona con la tabla de clientes
    total = Column(Float, nullable=False, default=0.0)
    fecha_venta = Column(TIMESTAMP, default=func.now(), nullable=False)

    # Relación con el modelo DetalleVenta
    detalles = relationship("DetalleVenta", back_populates="venta", cascade="all, delete-orphan")
