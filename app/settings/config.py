import os
import json
from pathlib import Path
from dotenv import load_dotenv

# Carga variables del archivo .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
#SETTINGS_DIR = BASE_DIR / "settings"
SETTINGS_DIR = BASE_DIR

# Lee el entorno desde .env (default: development)
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# Carga el archivo base + el específico del entorno
def load_config():
    with open(SETTINGS_DIR / "base.json") as f:
        base_config = json.load(f)
    with open(SETTINGS_DIR / f"{ENVIRONMENT}.json") as f:
        env_config = json.load(f)
    return {**base_config, **env_config}

# Construye configuración final
config = load_config()

# Ejemplo: construir la URL de la base de datos
DATABASE_URL = (
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
