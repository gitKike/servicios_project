# from fastapi import FastAPI
# from app.settings.config import DATABASE_URL, config  # 👈 importás la configuración
# from app.routes import categorias  # 👈 importás el archivo

# app = FastAPI()

# app.include_router(categorias.router)

# @app.get("/")
# def read_root():
#     return {
#         "message": "¡Hola desde FastAPI!",
#         "environment": config.get("name"),
#         "database_url": DATABASE_URL
#     }

from fastapi import FastAPI
from app.settings.config import config

from app.routes import productos
from app.routes import xproveedor
from app.routes import categorias
from app.routes import empaques
from app.routes import presentaciones
from app.routes import subcategorias
from app.routes import uventa


app = FastAPI()

# Agregar router
app.include_router(productos.router)
app.include_router(xproveedor.router)
app.include_router(categorias.router)
app.include_router(empaques.router)
app.include_router(presentaciones.router)
app.include_router(subcategorias.router)
app.include_router(uventa.router)


@app.get("/")
def read_root():
    return {
        "message": "¡Hola desde FastAPI!",
        "environment": config.get("name"),
        "database_url": config.get("DATABASE_URL")
    }

