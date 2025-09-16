from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.services.product_service import *
from app.schemas.product_schema import ProductoCreate, ProductoUpdate, ProductoResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import os

router = APIRouter()

security = HTTPBasic()

def verify_credentials(credentials: HTTPBasicCredentials):
    if credentials.username != os.getenv("API_USER") or credentials.password != os.getenv("API_PASSWORD"):
        raise HTTPException(status_code=401, detail="Acceso no autorizado")
    return credentials.username

@router.get("/productos", response_model=list[ProductoResponse])
def listar_productos(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    verify_credentials(credentials)
    return get_productos(db)

@router.get("/productos/{product_id}", response_model=ProductoResponse)
def obtener_producto(product_id: int, credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    verify_credentials(credentials)
    producto = get_producto(db, product_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/productos", response_model=ProductoResponse)
def crear_producto(producto: ProductoCreate, credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    verify_credentials(credentials)
    return create_producto(db, producto)

@router.put("/productos/{product_id}", response_model=ProductoResponse)
def actualizar_producto(product_id: int, producto: ProductoUpdate, credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    verify_credentials(credentials)
    return update_producto(db, product_id, producto)

@router.delete("/productos/{product_id}")
def eliminar_producto(product_id: int, credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    verify_credentials(credentials)
    return delete_producto(db, product_id)
