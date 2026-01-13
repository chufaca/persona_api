from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API de Personas")

# Modelo
class PersonaCreate(BaseModel):
    nombre: str
    edad: int

class Persona(BaseModel):
    id: int
    nombre: str
    edad: int

# Base de datos en memoria
personas_db: list[Persona] = []
contador_id = 1

# Endpoints
@app.get("/personas", response_model=list[Persona])
def obtener_personas():
    return personas_db

@app.get("/personas/{persona_id}", response_model=Persona)
def obtener_persona(persona_id: int):
    for persona in personas_db:
        if persona.id == persona_id:
            return persona
    raise HTTPException(status_code=404, detail="Persona no encontrada")

@app.post("/personas", response_model=Persona, status_code=201)
def crear_persona(persona: PersonaCreate):
    global contador_id
    nueva_persona = Persona(id=contador_id, nombre=persona.nombre, edad=persona.edad)
    personas_db.append(nueva_persona)
    contador_id += 1
    return nueva_persona
