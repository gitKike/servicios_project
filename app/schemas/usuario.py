from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID

from typing import List
from schemas.perfil import PerfilOut

class UsuarioBase(BaseModel):
    id_usuario: UUID
    email: Optional[EmailStr]
    nombre: Optional[str]
    ap_paterno: Optional[str]
    ap_materno: Optional[str]
    telefono: Optional[str]
    imagen_url: Optional[str]
    tipo_nodo: Optional[str]
    activo: bool

    class Config:
        orm_mode = True

class UsuarioCreate(BaseModel):
    email: EmailStr
    nombre: Optional[str]
    ap_paterno: Optional[str]
    ap_materno: Optional[str]
    telefono: Optional[str]
    imagen_url: Optional[str]

    id_usuario_padre: Optional[UUID]
    tipo_nodo: Optional[str] = "usuario"

    id_perfil: Optional[str]

class UsuarioUpdate(BaseModel):
    nombre: Optional[str]
    ap_paterno: Optional[str]
    ap_materno: Optional[str]
    telefono: Optional[str]
    imagen_url: Optional[str]
    activo: Optional[bool]
    id_perfil: Optional[str]

class UsuarioOut(UsuarioBase):
    perfil: Optional[PerfilOut]
    hijos: Optional[List["UsuarioOut"]] = None  # permite árboles

UsuarioOut.update_forward_refs()