from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

# Instanciamos las variables de entorno
load_dotenv()

# Configuración de la cadena de conexion a base de datos
DB_URL = (f"postgresql://{os.getenv('DB_USER')}:"
          f"{os.getenv('DB_PASSWORD')}@"
          f"{os.getenv('DB_HOST')}"
          f":{os.getenv('DB_PORT')}/"
          f"{os.getenv('DB_NAME')}")

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative Base para los modelos de SQLAlchemy
Base = declarative_base()

metadata = MetaData()

# Dependencia crear una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()