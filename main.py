from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models, schemas, crud
from database import SessionLocal

app = FastAPI(title="API de Notas con MySQL")

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/notas", response_model=list[schemas.Nota])
def api_obtener_notas(db: Session = Depends(get_db)):
    return crud.obtener_notas(db)

@app.get("/notas/{nota_id}", response_model=schemas.Nota)
def api_obtener_nota(nota_id: int, db: Session = Depends(get_db)):
    nota = crud.obtener_nota(db, nota_id)
    if not nota:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    return nota

@app.post("/notas", response_model=schemas.Nota, status_code=201)
def api_crear_nota(nota: schemas.NotaCreate, db: Session = Depends(get_db)):
    return crud.crear_nota(db, nota)

@app.put("/notas/{nota_id}", response_model=schemas.Nota)
def api_actualizar_nota(nota_id: int, datos: schemas.NotaCreate, db: Session = Depends(get_db)):
    nota = crud.actualizar_nota(db, nota_id, datos)
    if not nota:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    return nota

@app.delete("/notas/{nota_id}", status_code=204)
def api_eliminar_nota(nota_id: int, db: Session = Depends(get_db)):
    ok = crud.eliminar_nota(db, nota_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    return None
