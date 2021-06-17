from fastapi import FastAPI
import json

from starlette.responses import JSONResponse
app = FastAPI()

@app.get("/")



def read_root():
    jsonmensaje = {
        "Universidad": "UTPL", 
        "Curso": "Procesos de Ingeniería de Software", 
        "Alumno": "Fernando Javier León Alberca", 
        "Período": "Abr/Ago 2021", 
        "Lenguaje de programación preferido": "Typescript",
        "Aspiración PostGraduación": "Seguir estudiando con una maestria"
    }

    return jsonmensaje