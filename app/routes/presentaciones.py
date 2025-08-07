from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.separados.catpresentaciones import CatPresentaciones
from app.schemas.presentacion import PresentacionResponse

router = APIRouter(prefix="/presentaciones", tags=["presentaciones"])

@router.get("/", response_model=list[PresentacionResponse])
def listar_presentaciones(db: Session = Depends(get_db)):
    return db.query(CatPresentaciones).order_by(CatPresentaciones.presentacion).all()

