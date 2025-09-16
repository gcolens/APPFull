from sqlalchemy.orm import Session
from app.models.product_model import Producto
from app.schemas.product_schema import ProductoCreate, ProductoUpdate

def get_productos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Producto).offset(skip).limit(limit).all()

def get_producto(db: Session, product_id: int):
    return db.query(Producto).filter(Producto.id == product_id).first()

def create_producto(db: Session, producto: ProductoCreate):
    db_producto = Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def update_producto(db: Session, product_id: int, producto: ProductoUpdate):
    db_producto = db.query(Producto).filter(Producto.id == product_id).first()
    if not db_producto:
        return None
    for key, value in producto.dict().items():
        setattr(db_producto, key, value)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def delete_producto(db: Session, product_id: int):
    db_producto = db.query(Producto).filter(Producto.id == product_id).first()
    if db_producto:
        db.delete(db_producto)
        db.commit()
    return db_producto
