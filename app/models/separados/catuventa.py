from __future__ import annotations
from typing import Any, Optional, List, TYPE_CHECKING
from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, Numeric, ForeignKey, ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import text
from sqlalchemy.dialects.postgresql import DOMAIN
from app.database.db import Base
from app.database.custom_types import CITEXT

if TYPE_CHECKING: pass

class CatUventa(Base):
    __tablename__ = 'cat_uventa'
    __table_args__ = (
        PrimaryKeyConstraint('uventa', name='pk_cat_uventa'),
    )

    uventa: Mapped[Any] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False), primary_key=True)
    presentacion: Mapped[Optional[Any]] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False))

    cat_productos: Mapped[List['CatProductos']] = relationship('CatProductos', back_populates='cat_uventa')

