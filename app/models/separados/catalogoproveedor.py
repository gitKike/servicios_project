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

class CatalogoProveedor(Base):
    __tablename__ = 'catalogo_proveedor'
    __table_args__ = (
        ForeignKeyConstraint(['iditem'], ['items.iditem'], name='catalogo_proveedor_iditem_fkey'),
        ForeignKeyConstraint(['idproveedor'], ['cat_proveedores.idproveedor'], name='catalogo_proveedor_idproveedor_fkey'),
        PrimaryKeyConstraint('idcatalogo', name='catalogo_proveedor_pkey'),
        UniqueConstraint('idproveedor', 'iditem', name='catalogo_proveedor_idproveedor_iditem_key')
    )

    idcatalogo: Mapped[int] = mapped_column(Integer, primary_key=True)
    idproveedor: Mapped[Any] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False))
    iditem: Mapped[str] = mapped_column(Text)
    precio_venta: Mapped[decimal.Decimal] = mapped_column(Numeric(12, 2))
    fecha_alta: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))

    items: Mapped['Items'] = relationship('Items', back_populates='catalogo_proveedor')
    cat_proveedores: Mapped['CatProveedores'] = relationship('CatProveedores', back_populates='catalogo_proveedor')

