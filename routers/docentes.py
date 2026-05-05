from fastapi import APIRouter, HTTPException
from models import Docente, DocenteUpdate, DocenteDB
from database import SessionLocal


router = APIRouter(prefix="/docentes", tags=["Docentes"])


##################   GET   #########################

@router.get("/")
def get_alumnos(limit: int = 10):
    db = SessionLocal()
    docentes = db.query(DocenteDB).limit(limit).all()
    db.close()
    return docentes


@router.get("/{docente_id}")
def get_docente(docente_id: int):
    db = SessionLocal()
    docente = db.query(DocenteDB).filter(DocenteDB.id == docente_id).first()
    db.close()

    if not docente:
        raise HTTPException(status_code=404, detail="Docente no encontrado")

    return docente

##################   POST   #########################

@router.post("/")
def nuevo_docente(item: Docente):
    db = SessionLocal()

    nuevo = DocenteDB(**item.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    db.close()

    return nuevo

##################   PUT   #########################

@router.put("/{docente_id}")
def actualizar_docente(docente_id: int, item: Docente):
    db = SessionLocal()
    docente = db.query(DocenteDB).filter(DocenteDB.id == docente_id).first()

    if not docente:
        db.close()
        raise HTTPException(status_code=404, detail="Docente no encontrado")

    docente.nombre = item.nombre
    docente.edad = item.edad
    docente.grado = item.grado

    db.commit()
    db.refresh(docente)
    db.close()

    return docente

##################  PATCH   #########################

@router.patch("/{docente_id}")
def actualizar_parcial_docente(docente_id: int, item: DocenteUpdate):
    db = SessionLocal()
    docente = db.query(DocenteDB).filter(DocenteDB.id == docente_id).first()

    if not docente:
        db.close()
        raise HTTPException(status_code=404, detail="Docente no encontrado")

    update_data = item.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(docente, key, value)

    db.commit()
    db.refresh(docente)
    db.close()

    return docente

##################   DELETE   #########################


@router.delete("/{docente_id}")
def eliminar_docente(docente_id: int):
    db = SessionLocal()
    docente = db.query(DocenteDB).filter(DocenteDB.id == docente_id).first()

    if not docente:
        db.close()
        raise HTTPException(status_code=404, detail="Docente no encontrado")

    db.delete(docente)
    db.commit()
    db.close()

    return {"mensaje": "Docente eliminado correctamente"}