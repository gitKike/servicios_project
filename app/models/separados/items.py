from __future__ import annotations
from typing import Any, Optional, List, TYPE_CHECKING
from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, Numeric, ForeignKey, ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import text
from sqlalchemy.dialects.postgresql import DOMAIN
from app.database.db import Base
from app.database.custom_types import CITEXT

if TYPE_CHECKING: pass

class Items(Base):
    __tablename__ = 'items'
    __table_args__ = (
        CheckConstraint("tipo = ANY (ARRAY['producto'::text, 'servicio'::text])", name='items_tipo_check'),
        ForeignKeyConstraint(['idsubcategoria'], ['cat_subcategorias.idsubcategoria'], name='items_idsubcategoria_fkey'),
        PrimaryKeyConstraint('iditem', name='items_pkey')
    )

    iditem: Mapped[str] = mapped_column(Text, primary_key=True)
    nombre: Mapped[str] = mapped_column(Text)
    tipo: Mapped[str] = mapped_column(Text)
    idsubcategoria: Mapped[Any] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False))
    descripcion: Mapped[Optional[str]] = mapped_column(Text)
    unidad_venta: Mapped[Optional[str]] = mapped_column(Text)
    activo: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    cat_subcategorias: Mapped['CatSubcategorias'] = relationship('CatSubcategorias', back_populates='items')
    catalogo_proveedor: Mapped[List['CatalogoProveedor']] = relationship('CatalogoProveedor', back_populates='items')
    precios_items: Mapped[List['PreciosItems']] = relationship('PreciosItems', back_populates='items')

