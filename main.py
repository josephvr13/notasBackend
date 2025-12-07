from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import Nota
from schemas import NotaCreate, NotaResponse

# Crear las tablas automáticamente al iniciar la app
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Notas")

# -----------------------------
# Configuración CORS
# -----------------------------
origins = [
    "https://notasfrontend.vercel.app",  # reemplaza con la URL de tu frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # permite solicitudes desde tu frontend
    allow_credentials=True,
    allow_methods=["*"],         # permite GET, POST, PUT, DELETE
    allow_headers=["*"],
)

# -----------------------------
# RUTAS CRUD
# -----------------------------

# Crear una nota
@app.post("/notas", response_model=NotaResponse)
def crear_nota(nota: NotaCreate, db: Session = Depends(get_db)):
    nueva_nota = Nota(titulo=nota.titulo, contenido=nota.contenido)
    db.add(nueva_nota)
    db.commit()
    db.refresh(nueva_nota)
    return nueva_nota

# Listar todas las notas
@app.get("/notas", response_model=list[NotaResponse])
def obtener_notas(db: Session = Depends(get_db)):
    return db.query(Nota).all()

# Obtener nota por ID
@app.get("/notas/{nota_id}", response_model=NotaResponse)
def obtener_nota(nota_id: int, db: Session = Depends(get_db)):
    nota = db.query(Nota).filter(Nota.id == nota_id).first()
    if not nota:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    return nota

# Actualizar una nota
@app.put("/notas/{nota_id}", response_model=NotaResponse)
def actualizar_nota(nota_id: int, data: NotaCreate, db: Session = Depends(get_db)):
    nota = db.query(Nota).filter(Nota.id == nota_id).first()
    if not nota:
        raise HTTPException(status_code=404, detail="Nota no encontrada")

    nota.titulo = data.titulo
    nota.contenido = data.contenido
    db.commit()
    db.refresh(nota)
    return nota

# Eliminar una nota
@app.delete("/notas/{nota_id}")
def eliminar_nota(nota_id: int, db: Session = Depends(get_db)):
    nota = db.query(Nota).filter(Nota.id == nota_id).first()
    if not nota:
        raise HTTPException(status_code=404, detail="Nota no encontrada")

    db.delete(nota)
    db.commit()
    return {"mensaje": "Nota eliminada exitosamente"}
