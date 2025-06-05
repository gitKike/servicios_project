from __future__ import annotations
from typing import Any, Optional, List, TYPE_CHECKING
from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, Numeric, ForeignKey, ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import text
from sqlalchemy.dialects.postgresql import DOMAIN
from app.database.db import Base
from app.database.custom_types import CITEXT

# Opcional: imports de otras entidades para type checking
if TYPE_CHECKING:
    pass  # aquí puedes agregar from ... import ... si querés autocompletado

class CatCategorias(Base):
    __tablename__ = 'cat_categorias'
    __table_args__ = (
        PrimaryKeyConstraint('idcategoria', name='pk_cat_categorias'),
    )

    idcategoria: Mapped[Any] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False), primary_key=True)
    categoria: Mapped[Optional[Any]] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False))

    cat_subcategorias: Mapped[List['CatSubcategorias']] = relationship('CatSubcategorias', back_populates='cat_categorias')

