class Estudante:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

    def retornar_dados(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email
        }
    

class Disciplina:
    def __init__(self, codigo, nome, aulas_planejadas, aulas_ministradas):
        self.codigo = codigo
        self.nome = nome
        self.aulas_planejadas = aulas_planejadas 
        self.aulas_ministradas = aulas_ministradas

class Matricula:
    def __init__(self, id, estudante_id, disciplina_codigo, semestre, situacao):
        self.id = id
        self.estudante_id = estudante_id
        self.disciplina_codigo = disciplina_codigo
        self.semestre = semestre
        self.situacao = situacao

class Avaliacao:
    def __init__(self, id, disciplina_codigo, titulo):
        self.id = id
        self.disciplina_codigo = disciplina_codigo
        self.titulo = titulo

class Nota:
    def __init__(self, id, avaliacao_id, estudante_id, valor):
        self.id = id
        self.avaliacao_id = avaliacao_id
        self.estudante_id = estudante_id
        self.valor = valor

class Frequencia:
    def __init__(self, id, estudante_id, disciplina_codigo, presente):
        self.id = id
        self.disciplina_codigo = disciplina_codigo
        self.estudante_id = estudante_id
        self.presente = presente