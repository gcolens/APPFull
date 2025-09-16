from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from app.schemas.venta_detail_schema import DetalleVentaResponse

class VentaBase(BaseModel):
    cliente_id: int
    fecha_venta: Optional[datetime] = datetime.utcnow()
    total: float = 0.0

class VentaCreate(VentaBase):
    detalles: List[DetalleVentaResponse]

class VentaResponse(VentaBase):
    id: int
    detalles: List[DetalleVentaResponse]

    class Config:
        orm_mode = True
