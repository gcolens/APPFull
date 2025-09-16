from sqlalchemy.orm import Session
from app.models.client_model import Cliente
from app.schemas.client_schema import ClienteCreate, ClienteUpdate


# Metodos para listar y obtener un cliente en especifico de la base de datos -Get
def get_clientes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Cliente).offset(skip).limit(limit).all()

def get_cliente(db: Session, client_id: int):
    return db.query(Cliente).filter(Cliente.id == client_id).first()


# Metodos para crear un cliente en la Base de datos - Post
def create_cliente(db: Session, cliente: ClienteCreate):
    db_cliente = Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

# Métodos para actualizar información de los clientes segun su id - Put
def update_cliente(db: Session, client_id: int, cliente: ClienteUpdate):
    db_cliente = db.query(Cliente).filter(Cliente.id == client_id).first()
    if not db_cliente:
        return None
    for key, value in cliente.dict().items():
        setattr(db_cliente, key, value)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente


# Método para eliminar un cliente en la base de datos segun su identificacor - Delete
# este metodo se debe tener mucho cuidado, puede eliminar informacion importante de la BD
def delete_cliente(db: Session, client_id: int):
    db_cliente = db.query(Cliente).filter(Cliente.id == client_id).first()
    if db_cliente:
        db.delete(db_cliente)
        db.commit()
    return db_cliente
