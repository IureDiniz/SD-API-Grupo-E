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

@app.get("/disciplinas")
def disciplinas():
    return met.listar_disciplinas()

@app.get("/disciplinas/{id}")
def disciplina_id(id: int):
    return met.pegar_disciplina_por_id(id)

@app.get("/matriculas")
def matriculas():
    return met.listar_matriculas()

@app.get("/matriculas/{id}")
def matriculas_id(id: int):
    return met.pegar_matricula_por_id(id)

@app.get("/avaliacoes")
def avaliacoes():
    return met.listar_avaliacoes()

@app.get("/avaliacoes/{id}")
def avaliacoes_id(id: int):
    return met.pegar_avaliacao_por_id(id)

@app.get("/notas")
def notas():
    return met.listar_notas()

@app.get("/notas/{id}")
def notas_id(id: int):
    return met.pegar_nota_por_id(id)

@app.get("/frequencias")
def frequencias():
    return met.listar_frequencias()

@app.get("/frequencias/{id}")
def notas_id(id: int):
    return met.pegar_frequencia_por_id(id)
