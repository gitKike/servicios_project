from sqlalchemy import Table, Column, String
from sqlalchemy.orm import registry
from sqlalchemy.dialects.postgresql import CITEXT
from app.database.db import engine

mapper_registry = registry()

# Mapeo explícito a una tabla ya existente
@mapper_registry.mapped
class Categoria:
    __tablename__ = "cat_categorias"
    __table_args__ = {"schema": "public"}

    idcategoria: str
    categoria: str

    idcategoria = Column("idcategoria", CITEXT, primary_key=True)
    categoria = Column("categoria", CITEXT)