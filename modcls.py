from modfunc import gera_matricula

class Aluno:
    def __init__(self, nome_aluno):
        self.matricula = gera_matricula(5)
        self.nome = nome_aluno
