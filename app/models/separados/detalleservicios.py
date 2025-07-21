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

from app.models.separados.items import Items

if TYPE_CHECKING:
    from app.models.separados.items import Items

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

