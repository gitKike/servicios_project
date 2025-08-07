# app/schemas/categoria.py
from pydantic import BaseModel

class CategoriaResponse(BaseModel):
    idcategoria: str
    categoria: str | None = None

    class Config:
        orm_mode = True

