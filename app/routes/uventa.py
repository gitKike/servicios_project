from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.separados import CatUventa
from app.schemas.uventa import UventaResponse

router = APIRouter(prefix="/uventa", tags=["Unidad de venta"])

@router.get("/", response_model=list[UventaResponse])
def listar_uventa(db: Session = Depends(get_db)):
    return db.query(CatUventa).all()

