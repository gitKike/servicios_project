from __future__ import annotations
from typing import Any, Optional, List, TYPE_CHECKING
from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, Numeric, ForeignKey, ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import text
from sqlalchemy.dialects.postgresql import DOMAIN
from app.database.db import Base
from app.database.custom_types import CITEXT

if TYPE_CHECKING: pass

class CatProductos(Base):
    __tablename__ = 'cat_productos'
    __table_args__ = (
        ForeignKeyConstraint(['idempaque'], ['cat_empaques.empaque'], name='fk_cat_productos_cat_empaques1'),
        ForeignKeyConstraint(['idsubcategoria'], ['cat_subcategorias.idsubcategoria'], name='fk_cat_productos_cat_subcategorias'),
        ForeignKeyConstraint(['presentacion'], ['cat_presentaciones.presentacion'], name='fk_cat_productos_cat_presentaciones'),
        ForeignKeyConstraint(['uventa'], ['cat_uventa.uventa'], name='fk_cat_productos_cat_uventa'),
        PrimaryKeyConstraint('idproducto', name='pk_cat_productos')
    )

    idproducto: Mapped[Any] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False), primary_key=True)
    idclave: Mapped[Optional[Any]] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False))
    nombreproducto: Mapped[Optional[Any]] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False))
    idsubcategoria: Mapped[Optional[Any]] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False))
    idmarca: Mapped[Optional[Any]] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False))
    uventa: Mapped[Optional[Any]] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False))
    idindice: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    presentacion: Mapped[Optional[Any]] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False))
    presentacion_o_capacidad: Mapped[Optional[Any]] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False))
    idempaque: Mapped[Optional[Any]] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False))

    cat_empaques: Mapped[Optional['CatEmpaques']] = relationship('CatEmpaques', back_populates='cat_productos')
    cat_subcategorias: Mapped[Optional['CatSubcategorias']] = relationship('CatSubcategorias', back_populates='cat_productos')
    cat_presentaciones: Mapped[Optional['CatPresentaciones']] = relationship('CatPresentaciones', back_populates='cat_productos')
    cat_uventa: Mapped[Optional['CatUventa']] = relationship('CatUventa', back_populates='cat_productos')
    cat_xproveedor: Mapped[List['CatXproveedor']] = relationship('CatXproveedor', back_populates='cat_productos')
    precios_productos: Mapped[List['PreciosProductos']] = relationship('PreciosProductos', back_populates='cat_productos')

