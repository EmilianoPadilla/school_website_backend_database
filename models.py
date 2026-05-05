from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()



##################   ALUMNO   #########################

class Alumno(BaseModel):
    nombre: str
    edad: int
    grado: str

class AlumnoUpdate(BaseModel):
    nombre: Optional[str] = None
    edad: Optional[int] = None
    grado: Optional[str] = None

class AlumnoDB(Base):
    __tablename__ = "alumnos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    edad = Column(Integer)
    grado = Column(String)

##################   DOCENTE   #########################

class Docente(BaseModel):
    nombre: str
    materia: str
    anios_de_experiencia: int

class DocenteUpdate(BaseModel):
    nombre: Optional[str] = None
    materia: Optional[str] = None
    anios_de_experiencia: Optional[int] = None

class DocenteDB(Base):
    __tablename__ = "docentes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    materia = Column(String)
    anios_de_experiencia = Column(Integer)

##################   EVENTO   #########################

class Evento(BaseModel):
    titulo: str
    fecha: str
    ubicacion: str

class EventoUpdate(BaseModel):
    titulo: Optional[str] = None
    fecha: Optional[str] = None
    ubicacion: Optional[str] = None

class EventoDB(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    fecha = Column(String)
    ubicacion = Column(String)