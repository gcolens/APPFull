from sqlalchemy import Column, Integer, String, Text, DECIMAL, TIMESTAMP, func
from app.models.database import Base  # ❗️Importa el Base correcto

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    precio = Column(DECIMAL(10,2), nullable=False)
    stock = Column(Integer, nullable=False)
    fecha_creacion = Column(TIMESTAMP, default=func.now())
