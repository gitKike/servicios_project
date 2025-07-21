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

class CatProveedores(Base):
    __tablename__ = 'cat_proveedores'
    __table_args__ = (
        PrimaryKeyConstraint('idproveedor', name='pk_cat_proveedores'),
    )

    idproveedor: Mapped[Any] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False), primary_key=True)
    razon_social: Mapped[Any] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False))
    fecha_registro: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))

    cat_xproveedor: Mapped[List['CatXproveedor']] = relationship('CatXproveedor', back_populates='cat_proveedores')
    catalogo_proveedor: Mapped[List['CatalogoProveedor']] = relationship('CatalogoProveedor', back_populates='cat_proveedores')
    precios_items: Mapped[List['PreciosItems']] = relationship('PreciosItems', back_populates='cat_proveedores')
    precios_productos: Mapped[List['PreciosProductos']] = relationship('PreciosProductos', back_populates='cat_proveedores')

