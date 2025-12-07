from pydantic import BaseModel

class NotaCreate(BaseModel):
    titulo: str
    contenido: str

class NotaResponse(BaseModel):
    id: int
    titulo: str
    contenido: str
    creado_en: str

    class Config:
        orm_mode = True
