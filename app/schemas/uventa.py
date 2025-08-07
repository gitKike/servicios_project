from pydantic import BaseModel

class UventaResponse(BaseModel):
    uventa: str
    presentacion: str | None = None

    class Config:
        orm_mode = True

