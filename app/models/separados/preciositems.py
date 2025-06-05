from __future__ import annotations
from typing import Any, Optional, List, TYPE_CHECKING
from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, Numeric, ForeignKey, ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import text
from sqlalchemy.dialects.postgresql import DOMAIN
from app.database.db import Base
from app.database.custom_types import CITEXT

if TYPE_CHECKING: pass

class PreciosItems(Base):
    __tablename__ = 'precios_items'
    __table_args__ = (
        ForeignKeyConstraint(['iditem'], ['items.iditem'], name='precios_items_iditem_fkey'),
        ForeignKeyConstraint(['idproveedor'], ['cat_proveedores.idproveedor'], name='precios_items_idproveedor_fkey'),
        PrimaryKeyConstraint('idprecio', name='precios_items_pkey')
    )

    idprecio: Mapped[int] = mapped_column(Integer, primary_key=True)
    iditem: Mapped[str] = mapped_column(Text)
    precio: Mapped[decimal.Decimal] = mapped_column(Numeric(12, 2))
    idproveedor: Mapped[Optional[Any]] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False))
    fecha_registro: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))

    items: Mapped['Items'] = relationship('Items', back_populates='precios_items')
    cat_proveedores: Mapped[Optional['CatProveedores']] = relationship('CatProveedores', back_populates='precios_items')

