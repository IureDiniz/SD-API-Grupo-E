import database.conexao as conexao
import models.objetos as objetos
import json

def listar_estudantes():
    conexao.criar_bd()
    con = conexao.conectar_bd()
    cursor = con.cursor()
    cursor.execute("SELECT id, nome, email FROM estudantes")
    estudantes = cursor.fetchall()

    estudantes_objetos = [objetos.Estudante(id, nome, email) for id, nome, email in estudantes]

    return estudantes_objetos

def pegar_estudante_por_id(id):
    conexao.criar_bd()
    con = conexao.conectar_bd()
    cursor = con.cursor()
    cursor.execute("SELECT id, nome, email FROM estudantes WHERE id = %s", (id,))
    estudante = cursor.fetchone()

    if estudante:
        return objetos.Estudante(estudante[0], estudante[1], estudante[2])
    else:
        return None