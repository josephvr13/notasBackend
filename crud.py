from sqlalchemy.orm import Session
from models import Nota
import schemas

def obtener_notas(db: Session):
    return db.query(Nota).all()

def obtener_nota(db: Session, nota_id: int):
    return db.query(Nota).filter(Nota.id == nota_id).first()

def crear_nota(db: Session, nota: schemas.NotaCreate):
    nota_db = Nota(**nota.dict())
    db.add(nota_db)
    db.commit()
    db.refresh(nota_db)
    return nota_db

def actualizar_nota(db: Session, nota_id: int, datos: schemas.NotaCreate):
    nota = obtener_nota(db, nota_id)
    if nota:
        nota.titulo = datos.titulo
        nota.contenido = datos.contenido
        db.commit()
        db.refresh(nota)
        return nota
    return None

def eliminar_nota(db: Session, nota_id: int):
    nota = obtener_nota(db, nota_id)
    if nota:
        db.delete(nota)
        db.commit()
        return True
    return False
