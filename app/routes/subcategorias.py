from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.separados import CatSubcategorias
from app.schemas.subcategoria import SubcategoriaResponse

router = APIRouter(prefix="/subcategorias", tags=["Subcategorías"])

@router.get("/", response_model=list[SubcategoriaResponse])
def listar_subcategorias(db: Session = Depends(get_db)):
    return db.query(CatSubcategorias).all()

