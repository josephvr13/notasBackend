from sqlalchemy import Column, Integer, String, Text, DateTime, func
from database import Base  # Asegúrate que database.py está en la misma carpeta

class Nota(Base):
    __tablename__ = "notas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(200), nullable=False)
    contenido = Column(Text, nullable=False)
    creado_en = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Nota id={self.id} titulo={self.titulo}>"
