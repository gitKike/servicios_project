import uuid
from sqlalchemy import (
    Column, String, Boolean, Text, ForeignKey,
    DateTime
)
from sqlalchemy.dialects.postgresql import UUID, CITEXT
from sqlalchemy.orm import relationship
from datetime import datetime

#from app.core.db import Base    #Definir si es mediante app.core.db o mediante from app.database.db import Base
from app.database.db import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    # =============================
    # Identidad
    # =============================
    id_usuario = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(CITEXT, unique=True)

    nombre = Column(Text)
    ap_paterno = Column(Text)
    ap_materno = Column(Text)
    telefono = Column(Text)
    imagen_url = Column(Text)

    # =============================
    # Jerarquía
    # =============================
    id_usuario_padre = Column(UUID(as_uuid=True), ForeignKey("usuarios.id_usuario"), nullable=True)
    tipo_nodo = Column(String, default="usuario", nullable=False)

    padre = relationship("Usuario", remote_side=[id_usuario], backref="hijos")

    # =============================
    # Perfil / Rol
    # =============================
    id_perfil = Column(String(4), ForeignKey("perfiles.id_perfil"))
    perfil = relationship("Perfil", back_populates="usuarios")

    # =============================
    # OAuth
    # =============================
    proveedor_oauth = Column(String)  # google, facebook, microsoft, interno
    id_externo = Column(String, unique=False)  # se controla por índice SQL

    # =============================
    # Estado y auditoría
    # =============================
    activo = Column(Boolean, default=True, nullable=False)
    ultimo_login = Column(DateTime(timezone=True))

    fecha_creacion = Column(DateTime(timezone=True), default=datetime.utcnow)
    fecha_modificacion = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
    fecha_inactivacion = Column(DateTime(timezone=True), nullable=True)
