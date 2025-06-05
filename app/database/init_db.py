from sqlalchemy.orm import Session
from app.database.db import Base, engine
from app.models import separados  # ⬅️ importa los modelos para que SQLAlchemy los registre

def init_db():
    """
    Crea todas las tablas definidas en los modelos si no existen.
    Ideal para usar en ambientes de desarrollo o testing.
    """
    Base.metadata.create_all(bind=engine)
