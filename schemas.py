from pydantic import BaseModel
from datetime import datetime

class NotaBase(BaseModel):
    titulo: str
    contenido: str

class NotaCreate(NotaBase):
    pass

class Nota(NotaBase):
    id: int
    creado_en: datetime | None = None

    class Config:
        orm_mode = True
