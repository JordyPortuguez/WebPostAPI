from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy.engine import URL

CadenaConexion=URL.create(
    drivername="postgresql",
    username="postgres",
    password="postgres",
    host="localhost",
    database="postgres",
    port=5432,
)

Engine=create_engine(CadenaConexion)
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=Engine)
Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
