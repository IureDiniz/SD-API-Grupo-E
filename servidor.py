from fastapi import FastAPI
import models.metodos as met

app = FastAPI()

@app.get("/")
def home():
    return "Minha API está no ar"

@app.get("/estudantes")
def estudantes():
    return met.listar_estudantes()

@app.get("/estudantes/{id}")
def estudante_id(id: int):
    return met.pegar_estudante_por_id(id)