from pydantic import BaseModel

class EmpaqueResponse(BaseModel):
    empaque: str
    abreviatura: str

    class Config:
        orm_mode = True

