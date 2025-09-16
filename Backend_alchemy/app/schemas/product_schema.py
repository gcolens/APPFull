from pydantic import BaseModel, condecimal
from typing import Optional
from datetime import datetime

class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: condecimal(max_digits=10, decimal_places=2)
    stock: int

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    pass

class ProductoResponse(ProductoBase):
    id: int
    fecha_creacion: datetime

    class Config:
        orm_mode = True
