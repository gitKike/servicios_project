from pydantic import BaseModel

class PerfilBase(BaseModel):
    id_perfil: str
    nombre: str
    smart: bool

    class Config:
        orm_mode = True


class PerfilCreate(BaseModel):
    id_perfil: str
    nombre: str
    smart: bool = False


class PerfilOut(PerfilBase):
    pass
