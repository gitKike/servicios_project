from typing import Any, List, Optional

from sqlalchemy import Boolean, CheckConstraint, DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, Text, UniqueConstraint, text
from sqlalchemy.dialects.postgresql import DOMAIN
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from app.database.custom_types import CITEXT

import datetime
import decimal

class Base(DeclarativeBase):
    pass


class CatCategorias(Base):
    __tablename__ = 'cat_categorias'
    __table_args__ = (
        PrimaryKeyConstraint('idcategoria', name='pk_cat_categorias'),
    )

    idcategoria: Mapped[Any] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False), primary_key=True)
    categoria: Mapped[Optional[Any]] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False))

    cat_subcategorias: Mapped[List['CatSubcategorias']] = relationship('CatSubcategorias', back_populates='cat_categorias')


class CatEmpaques(Base):
    __tablename__ = 'cat_empaques'
    __table_args__ = (
        PrimaryKeyConstraint('empaque', name='pk_cat_empaque'),
    )

    empaque: Mapped[Any] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False), primary_key=True)
    abreviatura: Mapped[Any] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False))

    cat_productos: Mapped[List['CatProductos']] = relationship('CatProductos', back_populates='cat_empaques')


class CatPresentaciones(Base):
    __tablename__ = 'cat_presentaciones'
    __table_args__ = (
        PrimaryKeyConstraint('presentacion', name='pk_cat_presentaciones'),
    )

    presentacion: Mapped[Any] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False), primary_key=True)

    cat_productos: Mapped[List['CatProductos']] = relationship('CatProductos', back_populates='cat_presentaciones')


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


class CatUventa(Base):
    __tablename__ = 'cat_uventa'
    __table_args__ = (
        PrimaryKeyConstraint('uventa', name='pk_cat_uventa'),
    )

    uventa: Mapped[Any] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False), primary_key=True)
    presentacion: Mapped[Optional[Any]] = mapped_column(DOMAIN('case_insensitive_text', CITEXT(), not_null=False))

    cat_productos: Mapped[List['CatProductos']] = relationship('CatProductos', back_populates='cat_uventa')


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


class DetalleProductos(Items):
    __tablename__ = 'detalle_productos'
    __table_args__ = (
        ForeignKeyConstraint(['iditem'], ['items.iditem'], ondelete='CASCADE', name='detalle_productos_iditem_fkey'),
        PrimaryKeyConstraint('iditem', name='detalle_productos_pkey')
    )

    iditem: Mapped[str] = mapped_column(Text, primary_key=True)
    marca: Mapped[Optional[str]] = mapped_column(Text)
    modelo: Mapped[Optional[str]] = mapped_column(Text)
    especificaciones: Mapped[Optional[str]] = mapped_column(Text)


class DetalleServicios(Items):
    __tablename__ = 'detalle_servicios'
    __table_args__ = (
        ForeignKeyConstraint(['iditem'], ['items.iditem'], ondelete='CASCADE', name='detalle_servicios_iditem_fkey'),
        PrimaryKeyConstraint('iditem', name='detalle_servicios_pkey')
    )

    iditem: Mapped[str] = mapped_column(Text, primary_key=True)
    tipo_servicio: Mapped[Optional[str]] = mapped_column(Text)
    duracion_estimada: Mapped[Optional[str]] = mapped_column(Text)
    requiere_visita: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('false'))


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
