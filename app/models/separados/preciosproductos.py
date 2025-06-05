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

class PreciosProductos(Base):
    __tablename__ = 'precios_productos'
    __table_args__ = (
        ForeignKeyConstraint(['idproducto'], ['cat_productos.idproducto'], ondelete='CASCADE', onupdate='CASCADE', name='fk_precio_producto'),
        ForeignKeyConstraint(['idproveedor'], ['cat_proveedores.idproveedor'], ondelete='CASCADE', onupdate='CASCADE', name='fk_precio_proveedor'),
        PrimaryKeyConstraint('idprecio', name='precios_productos_pkey')
    )

    idprecio: Mapped[int] = mapped_column(Integer, primary_key=True)
    idproducto: Mapped[Any] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False))
    idproveedor: Mapped[Any] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False))
    precio: Mapped[decimal.Decimal] = mapped_column(Numeric(12, 2))
    fecha_registro: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))

    cat_productos: Mapped['CatProductos'] = relationship('CatProductos', back_populates='precios_productos')
    cat_proveedores: Mapped['CatProveedores'] = relationship('CatProveedores', back_populates='precios_productos')