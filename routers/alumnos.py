from fastapi import APIRouter, HTTPException
from models import Alumno, AlumnoUpdate, AlumnoDB
from database import SessionLocal

router = APIRouter(prefix="/alumnos", tags=["Alumnos"])


##################   GET   #########################

@router.get("/")
def get_alumnos(limit: int = 10):
    db = SessionLocal()
    alumnos = db.query(AlumnoDB).limit(limit).all()
    db.close()
    return alumnos


@router.get("/{alumno_id}")
def get_alumno(alumno_id: int):
    db = SessionLocal()
    alumno = db.query(AlumnoDB).filter(AlumnoDB.id == alumno_id).first()
    db.close()

    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")

    return alumno

##################   POST   #########################

@router.post("/")
def nuevo_alumno(item: Alumno):
    db = SessionLocal()

    nuevo = AlumnoDB(**item.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    db.close()

    return nuevo

##################   PUT   #########################    

@router.put("/{alumno_id}")
def actualizar_alumno(alumno_id: int, item: Alumno):
    db = SessionLocal()
    alumno = db.query(AlumnoDB).filter(AlumnoDB.id == alumno_id).first()

    if not alumno:
        db.close()
        raise HTTPException(status_code=404, detail="Alumno no encontrado")

    alumno.nombre = item.nombre
    alumno.edad = item.edad
    alumno.grado = item.grado

    db.commit()
    db.refresh(alumno)
    db.close()

    return alumno
##################   PATCH   #########################

@router.patch("/{alumno_id}")
def actualizar_parcial_alumno(alumno_id: int, item: AlumnoUpdate):
    db = SessionLocal()
    alumno = db.query(AlumnoDB).filter(AlumnoDB.id == alumno_id).first()

    if not alumno:
        db.close()
        raise HTTPException(status_code=404, detail="Alumno no encontrado")

    update_data = item.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(alumno, key, value)

    db.commit()
    db.refresh(alumno)
    db.close()

    return alumno

##################   DELETE   #########################


@router.delete("/{alumno_id}")
def eliminar_alumno(alumno_id: int):
    db = SessionLocal()
    alumno = db.query(AlumnoDB).filter(AlumnoDB.id == alumno_id).first()

    if not alumno:
        db.close()
        raise HTTPException(status_code=404, detail="Alumno no encontrado")

    db.delete(alumno)
    db.commit()
    db.close()

    return {"mensaje": "Alumno eliminado correctamente"}