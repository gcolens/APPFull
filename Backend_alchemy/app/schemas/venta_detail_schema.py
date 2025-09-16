from pydantic import BaseModel
from typing import Optional

class DetalleVentaBase(BaseModel):
    producto_id: int
    cantidad: int
    precio_unitario: float
    subtotal: float

class DetalleVentaCreate(DetalleVentaBase):
    pass

class DetalleVentaResponse(DetalleVentaBase):
    id: int
    venta_id: int

    class Config:
        orm_mode = True
