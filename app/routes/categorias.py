from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database.db import get_session
from app.models.categorias import Categoria

router = APIRouter()

@router.get("/categorias")
async def get_categorias(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Categoria))
    return result.scalars().all()
