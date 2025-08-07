# from typing import Optional
# from pydantic import BaseModel


# class ProductoResponse(BaseModel):
#     idproducto: str
#     idclave: Optional[str]
#     nombreproducto: Optional[str]
#     idsubcategoria: Optional[str]
#     idmarca: Optional[str]
#     uventa: Optional[str]
#     idindice: Optional[int]
#     presentacion: Optional[str]
#     presentacion_o_capacidad: Optional[str]
#     idempaque: Optional[str]

#     class Config:
#         orm_mode = True

from pydantic import BaseModel

class ProductoResponse(BaseModel):
    idproducto: str
    idclave: str | None = None
    nombreproducto: str | None = None
    idsubcategoria: str | None = None
    idmarca: str | None = None
    uventa: str | None = None
    idindice: int | None = None
    presentacion: str | None = None
    presentacion_o_capacidad: str | None = None
    idempaque: str | None = None

    class Config:
        orm_mode = True

