from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.separados import CatXproveedor
from app.schemas.xproveedor import XProveedorCreate, XProveedorResponse

router = APIRouter(prefix="/xproveedor", tags=["XProveedor"])


@router.post("/", response_model=XProveedorResponse, status_code=201)
def registrar_producto_proveedor(payload: XProveedorCreate, db: Session = Depends(get_db)):
    existente = db.query(CatXproveedor).filter_by(
        idproducto=payload.idproducto,
        idproveedor=payload.idproveedor
    ).first()

    if existente:
        raise HTTPException(status_code=400, detail="Ya existe ese producto para el proveedor")

    nuevo = CatXproveedor(**payload.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
