from fastapi import APIRouter, HTTPException
from models import Evento, EventoUpdate, EventoDB, EventoResponse
from database import SessionLocal


router = APIRouter(prefix="/eventos", tags=["Eventos"])


##################   GET   #########################

@router.get("/", response_model=list[EventoResponse])
def get_eventos(limit: int = 10, offset: int = 0):
    db = SessionLocal()
    eventos = (
        db.query(EventoDB)
        .order_by(EventoDB.id)
        .limit(limit)
        .offset(offset)
        .all()
    )
    db.close()
    return eventos


@router.get("/{evento_id}")
def get_evento(evento_id: int):
    db = SessionLocal()
    evento = (
        db.query(EventoDB)
        .filter(EventoDB.id == evento_id)
        .first()
    )
    
    if not evento:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    
    db.close()
    return evento


##################   POST   #########################

@router.post("/")
def nuevo_evento(item: Evento):
    db = SessionLocal()

    nuevo = EventoDB(**item.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    db.close()

    return nuevo


##################   PUT   #########################

@router.put("/{evento_id}")
def actualizar_evento(evento_id: int, item: Evento):
    db = SessionLocal()
    evento = db.query(EventoDB).filter(EventoDB.id == evento_id).first()

    if not evento:
        db.close()
        raise HTTPException(status_code=404, detail="Evento no encontrado")

    evento.titulo = item.titulo
    evento.fecha = item.fecha
    evento.ubicacion = item.ubicacion

    db.commit()
    db.refresh(evento)
    db.close()

    return evento


##################   PATCH   #########################

@router.patch("/{evento_id}")
def actualizar_parcial_evento(evento_id: int, item: EventoUpdate):
    db = SessionLocal()
    evento = db.query(EventoDB).filter(EventoDB.id == evento_id).first()

    if not evento:
        db.close()
        raise HTTPException(status_code=404, detail="Evento no encontrado")

    update_data = item.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(evento, key, value)

    db.commit()
    db.refresh(evento)
    db.close()

    return evento


##################   DELETE   #########################

@router.delete("/{evento_id}")
def eliminar_evento(evento_id: int):
    db = SessionLocal()
    evento = db.query(EventoDB).filter(EventoDB.id == evento_id).first()

    if not evento:
        db.close()
        raise HTTPException(status_code=404, detail="Evento no encontrado")

    db.delete(evento)
    db.commit()
    db.close()

    return {"mensaje": "Evento eliminado correctamente"}