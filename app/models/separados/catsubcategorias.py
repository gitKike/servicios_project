from __future__ import annotations
import decimal
import datetime
import uuid
from typing import Any, Optional, List, TYPE_CHECKING
from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, Numeric, ForeignKey, ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import text
from sqlalchemy.dialects.postgresql import DOMAIN
from app.database.db import Base
from app.database.custom_types import CITEXT


if TYPE_CHECKING:
    pass

class CatSubcategorias(Base):
    __tablename__ = 'cat_subcategorias'
    __table_args__ = (
        ForeignKeyConstraint(['idcategoria'], ['cat_categorias.idcategoria'], name='fk_cat_subcategorias_cat_categorias1'),
        PrimaryKeyConstraint('idsubcategoria', name='pk_cat_subcategorias')
    )

    idsubcategoria: Mapped[Any] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False), primary_key=True)
    idcategoria: Mapped[Any] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False))
    subcategoria: Mapped[Optional[Any]] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False))

    cat_categorias: Mapped['CatCategorias'] = relationship('CatCategorias', back_populates='cat_subcategorias')
    cat_productos: Mapped[List['CatProductos']] = relationship('CatProductos', back_populates='cat_subcategorias')
    items: Mapped[List['Items']] = relationship('Items', back_populates='cat_subcategorias')

