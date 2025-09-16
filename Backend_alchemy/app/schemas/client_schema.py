from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class ClienteBase(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    telefono: Optional[str]
    direccion: Optional[str]

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    id: int
    fecha_registro: datetime

    class Config:
        orm_mode = True
