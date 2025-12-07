from sqlalchemy.orm import Session
from models import Nota
import schemas

def obtener_notas(db: Session):
    return db.query(Nota).order_by(Nota.id.desc()).all()

def obtener_nota(db: Session, nota_id: int):
    return db.query(Nota).filter(Nota.id == nota_id).first()

def crear_nota(db: Session, nota: schemas.NotaCreate):
    nueva_nota = Nota(
        titulo=nota.titulo,
        contenido=nota.contenido
    )
    db.add(nueva_nota)
    db.commit()
    db.refresh(nueva_nota)
    return nueva_nota

def actualizar_nota(db: Session, nota_id: int, datos: schemas.NotaCreate):
    nota = obtener_nota(db, nota_id)
    if not nota:
        return None

    nota.titulo = datos.titulo
    nota.contenido = datos.contenido

    db.commit()
    db.refresh(nota)
    return nota

def eliminar_nota(db: Session, nota_id: int):
    nota = obtener_nota(db, nota_id)
    if not nota:
        return False

    db.delete(nota)
    db.commit()
    return True
