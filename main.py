from fastapi import FastAPI
from routers import alumnos, docentes, eventos

from database import engine
from models import Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Bienvenido a nuestra página escolar!"}

app.include_router(alumnos.router)
app.include_router(docentes.router)
app.include_router(eventos.router)