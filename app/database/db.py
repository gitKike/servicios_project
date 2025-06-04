from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.settings.config import DATABASE_URL

# Cambia el esquema de URL a asyncpg para conexión asíncrona
ASYNC_DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

# Crear engine
engine = create_async_engine(ASYNC_DATABASE_URL, echo=True)

# Crear sessionmaker
async_session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# Dependency para FastAPI
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session