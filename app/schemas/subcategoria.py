from pydantic import BaseModel

class SubcategoriaResponse(BaseModel):
    idsubcategoria: str
    idcategoria: str
    subcategoria: str | None = None

    class Config:
        orm_mode = True

