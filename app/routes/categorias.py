# app/routes/categorias.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.separados.catcategorias import CatCategorias
from app.schemas.categoria import CategoriaResponse

router = APIRouter(prefix="/categorias", tags=["categorias"])

@router.get("/", response_model=list[CategoriaResponse])
def listar_categorias(db: Session = Depends(get_db)):
    return db.query(CatCategorias).order_by(CatCategorias.categoria).all()
