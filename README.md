# Persona API

API REST simple en Python para gestionar personas.

## Tech Stack

- **FastAPI** - Framework web moderno y rápido
- **Pydantic** - Validación de datos
- **Uvicorn** - Servidor ASGI

## Instalación

```bash
pip install fastapi uvicorn
```

## Uso

```bash
uvicorn main:app --reload
```

El servidor corre en `http://localhost:8000`

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/personas` | Listar todas las personas |
| GET | `/personas/{id}` | Obtener persona por ID |
| POST | `/personas` | Crear nueva persona |

## Ejemplos

**Crear persona:**
```bash
curl -X POST http://localhost:8000/personas \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Juan", "edad": 30}'
```

**Listar personas:**
```bash
curl http://localhost:8000/personas
```

**Obtener persona por ID:**
```bash
curl http://localhost:8000/personas/1
```

## Documentación

FastAPI genera documentación automática:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
