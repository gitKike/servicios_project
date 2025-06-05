from __future__ import annotations
from typing import Any, Optional, List, TYPE_CHECKING
from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, Numeric, ForeignKey, ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import text
from sqlalchemy.dialects.postgresql import DOMAIN
from app.database.db import Base
from app.database.custom_types import CITEXT

if TYPE_CHECKING: pass

class CatXproveedor(Base):
    __tablename__ = 'cat_xproveedor'
    __table_args__ = (
        ForeignKeyConstraint(['idproducto'], ['cat_productos.idproducto'], ondelete='CASCADE', onupdate='CASCADE', name='fk_cat_xproveedor_producto'),
        ForeignKeyConstraint(['idproveedor'], ['cat_proveedores.idproveedor'], ondelete='CASCADE', onupdate='CASCADE', name='fk_cat_xproveedor_proveedor'),
        PrimaryKeyConstraint('idproveedor', 'idproducto', name='pk_cat_xproveedor')
    )

    idproveedor: Mapped[Any] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False), primary_key=True)
    idproducto: Mapped[Any] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False), primary_key=True)
    fecha_registro: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))

    cat_productos: Mapped['CatProductos'] = relationship('CatProductos', back_populates='cat_xproveedor')
    cat_proveedores: Mapped['CatProveedores'] = relationship('CatProveedores', back_populates='cat_xproveedor')

