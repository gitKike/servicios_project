from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.separados.catempaques import CatEmpaques
from app.schemas.empaque import EmpaqueResponse

router = APIRouter(prefix="/empaques", tags=["empaques"])

@router.get("/", response_model=list[EmpaqueResponse])
def listar_empaques(db: Session = Depends(get_db)):
    return db.query(CatEmpaques).order_by(CatEmpaques.empaque).all()

