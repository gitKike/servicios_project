from fastapi import FastAPI
from app.settings.config import DATABASE_URL, config  # 👈 importás la configuración
from app.routes import categorias  # 👈 importás el archivo

app = FastAPI()

app.include_router(categorias.router)

@app.get("/")
def read_root():
    return {
        "message": "¡Hola desde FastAPI!",
        "environment": config.get("name"),
        "database_url": DATABASE_URL
    }
