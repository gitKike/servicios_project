from pydantic import BaseModel

class PresentacionResponse(BaseModel):
    presentacion: str

    class Config:
        orm_mode = True

