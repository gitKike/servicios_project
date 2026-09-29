
# Servicios API 🚀

API desarrollada con [FastAPI](https://fastapi.tiangolo.com/) para gestionar servicios.

---

## 🧱 Estructura del proyecto

```
servicios_project/
├── app/
│   ├── main.py               # Punto de entrada de la app
│   ├── config.py             # Carga configuración desde .env y .json
│   └── settings/             # Configuraciones por entorno
├── .env                      # Variables sensibles (no subir al repo)
├── requirements.txt          # Dependencias
└── venv/                     # Entorno virtual (ignorado por git)
```

---

## ⚙️ Configuración

1. Crea un archivo `.env` en la raíz del proyecto, basado en el `.env.example`:

```
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_db
ENVIRONMENT=development
```

2. Verifica que existan los archivos en `app/settings/`:
   - `base.json`
   - `development.json`
   - `production.json`

---

## 🚀 Ejecución

### Crear entorno virtual e instalar dependencias:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Iniciar el servidor de desarrollo:

```bash
uvicorn app.main:app --reload
```

Por defecto, la app estará disponible en:  
👉 http://127.0.0.1:8000  
👉 Documentación Swagger: http://127.0.0.1:8000/docs

---

## 🧪 Pruebas

*Por ahora no hay pruebas automatizadas. Próximamente...*

---

## 🛠 Tecnologías usadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [Uvicorn](https://www.uvicorn.org/)

---

## ✍️ Autor

**Kike**  
📫 spin-e@outlook.com
📫 kotonete.kid@outlook.com
