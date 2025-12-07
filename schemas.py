from pydantic import BaseModel
from datetime import datetime

class NotaCreate(BaseModel):
    titulo: str
    contenido: str

class NotaResponse(BaseModel):
    id: int
    titulo: str
    contenido: str
    creado_en: datetime  # ← corregido

    class Config:
        orm_mode = True
