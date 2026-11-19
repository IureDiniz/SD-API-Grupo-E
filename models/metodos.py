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


def listar_disciplinas():
    conexao.criar_bd()
    con = conexao.conectar_bd()
    cursor = con.cursor()
    cursor.execute("SELECT codigo, nome, aulas_planejadas, aulas_ministradas FROM disciplinas")
    disciplinas = cursor.fetchall()

    disciplinas_objetos = [
        objetos.Disciplina(codigo, nome, aulas_planejadas, aulas_ministradas)
        for codigo, nome, aulas_planejadas, aulas_ministradas in disciplinas
    ]

    return disciplinas_objetos

def pegar_disciplina_por_id(id):
    conexao.criar_bd()
    con = conexao.conectar_bd()
    cursor = con.cursor()
    cursor.execute("SELECT codigo, nome, aulas_planejadas, aulas_ministradas FROM disciplinas WHERE codigo = %s", (id,))
    disciplina = cursor.fetchone()

    if disciplina:
        return objetos.Disciplina(disciplina[0], disciplina[1], disciplina[2], disciplina[3])
    else:
        return None

def listar_matriculas():
    conexao.criar_bd()
    con = conexao.conectar_bd()
    cursor = con.cursor()
    cursor.execute("SELECT id, estudante_id, disciplina_codigo, semestre, situacao FROM matriculas")
    matriculas = cursor.fetchall()

    matriculas_objetos = [
        objetos.Matricula(id, estudante_id, disciplina_codigo, semestre, situacao)
        for id, estudante_id, disciplina_codigo, semestre, situacao in matriculas
    ]

    return matriculas_objetos

def pegar_matricula_por_id(id):
    conexao.criar_bd()
    con = conexao.conectar_bd()
    cursor = con.cursor()
    cursor.execute("SELECT id, estudante_id, disciplina_codigo, semestre, situacao FROM matriculas WHERE id = %s", (id,))
    matricula = cursor.fetchone()

    if matricula:
        return objetos.Matricula(matricula[0], matricula[1], matricula[2], matricula[3], matricula[4])
    else:
        return None

def listar_avaliacoes():
    conexao.criar_bd()
    con = conexao.conectar_bd()
    cursor = con.cursor()
    cursor.execute("SELECT id, disciplina_codigo, titulo FROM avaliacoes")
    avaliacoes = cursor.fetchall()

    avaliacoes_objetos = [
        objetos.Avaliacao(id, disciplina_codigo, titulo)
        for id, disciplina_codigo, titulo in avaliacoes
    ]

    return avaliacoes_objetos

def pegar_avaliacao_por_id(id):
    conexao.criar_bd()
    con = conexao.conectar_bd()
    cursor = con.cursor()
    cursor.execute("SELECT id, disciplina_codigo, titulo FROM avaliacoes WHERE id = %s", (id,))
    avaliacao = cursor.fetchone()

    if avaliacao:
        return objetos.Avaliacao(avaliacao[0], avaliacao[1], avaliacao[2])
    else:
        return None

def listar_notas():
    conexao.criar_bd()
    con = conexao.conectar_bd()
    cursor = con.cursor()
    cursor.execute("SELECT id, avaliacao_id, estudante_id, valor FROM notas")
    notas = cursor.fetchall()

    notas_objetos = [
        objetos.Nota(id, avaliacao_id, estudante_id, valor)
        for id, avaliacao_id, estudante_id, valor in notas
    ]

    return notas_objetos

def pegar_nota_por_id(id):
    conexao.criar_bd()
    con = conexao.conectar_bd()
    cursor = con.cursor()
    cursor.execute("SELECT id, avaliacao_id, estudante_id, valor FROM notas WHERE id = %s", (id,))
    nota = cursor.fetchone()

    if nota:
        return objetos.Nota(nota[0], nota[1], nota[2], nota[3])
    else:
        return None

def listar_frequencias():
    conexao.criar_bd()
    con = conexao.conectar_bd()
    cursor = con.cursor()
    cursor.execute("SELECT id, estudante_id, disciplina_codigo, aulas_presente FROM frequencia")
    frequencias = cursor.fetchall()

    frequencias_objetos = [
        objetos.Frequencia(id, estudante_id, disciplina_codigo, aulas_presente)
        for id, estudante_id, disciplina_codigo, aulas_presente in frequencias
    ]

    return frequencias_objetos

def pegar_frequencia_por_id(id):
    conexao.criar_bd()
    con = conexao.conectar_bd()
    cursor = con.cursor()
    cursor.execute("SELECT id, estudante_id, disciplina_codigo, aulas_presente FROM frequencia WHERE id = %s", (id,))
    frequencia = cursor.fetchone()

    if frequencia:
        return objetos.Frequencia(frequencia[0], frequencia[1], frequencia[2], frequencia[3])
    else:
        return None
