from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.settings.config import DATABASE_URL

# Crear el engine (conexió a la base)
engine = create_engine(DATABASE_URL, echo=True)

# Sesión para interactuar con la DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para declarar modelos
Base = declarative_base()


