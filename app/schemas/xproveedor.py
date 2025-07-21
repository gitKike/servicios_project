from typing import Optional
from pydantic import BaseModel, Field
from decimal import Decimal


class XProveedorCreate(BaseModel):
    idproducto: str
    idproveedor: str
    precio_venta: Decimal = Field(..., gt=0)
    estatus: Optional[str] = "activo"


class XProveedorResponse(XProveedorCreate):
    idproducto: str
    idproveedor: str

    class Config:
        orm_mode = True
