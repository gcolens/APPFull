from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session

from app.models.database import get_db
from app.schemas.venta_schema import VentaCreate, VentaResponse
from app.services.venta_service import VentasService

import os

router = APIRouter()
security = HTTPBasic()

# Verificación de credenciales
def verify_credentials(credentials: HTTPBasicCredentials):
    if credentials.username != os.getenv("API_USER") or credentials.password != os.getenv("API_PASSWORD"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Acceso no autorizado")
    return credentials.username

# Listar todas las ventas
@router.get("/", response_model=list[VentaResponse], status_code=status.HTTP_200_OK)
def listar_ventas(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    verify_credentials(credentials)
    return VentasService.get_ventas(db)

# Obtener una venta específica
@router.get("/{venta_id}", response_model=VentaResponse, status_code=status.HTTP_200_OK)
def obtener_venta(venta_id: int, credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    verify_credentials(credentials)
    venta = VentasService.get_venta(db, venta_id)
    if not venta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Venta no encontrada")
    return venta

# Actualizar una venta existente
@router.put("/{venta_id}", response_model=VentaResponse, status_code=status.HTTP_200_OK)
def actualizar_venta(venta_id: int, venta: VentaCreate, credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    verify_credentials(credentials)
    return VentasService.update_venta(db, venta_id, venta)

# Eliminar una venta
@router.delete("/{venta_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_venta(venta_id: int, credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    verify_credentials(credentials)
    VentasService.delete_venta(db, venta_id)
