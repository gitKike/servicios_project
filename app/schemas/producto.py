from typing import Optional
from pydantic import BaseModel


class ProductoResponse(BaseModel):
    idproducto: str
    idclave: Optional[str]
    nombreproducto: Optional[str]
    idsubcategoria: Optional[str]
    idmarca: Optional[str]
    uventa: Optional[str]
    idindice: Optional[int]
    presentacion: Optional[str]
    presentacion_o_capacidad: Optional[str]
    idempaque: Optional[str]

    class Config:
        orm_mode = True
