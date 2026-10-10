from disciplina import Disciplina
class Aluno:
    def __init__(self, nome, rm, curso):
        self.nome = nome
        self.rm = rm
        self.curso = curso
        self.disciplinas = []           # [Disciplina, Disciplina,...]
        self.notas_por_disciplina = {}  # {"nome_d": [nota1, nota2,...],...}

    def matricular(self, disciplina: Disciplina):
        self.disciplinas.append(disciplina)
        self.notas_por_disciplina.setdefault(disciplina.nome, [])

    def adicionar_nota(self, d: Disciplina, nota: float):
        self.notas_por_disciplina[d.nome].append(nota)

    def calcular_media_d(self, d: Disciplina) -> float:
        notas = self.notas_por_disciplina.get(d.nome, [])
        return sum(notas) / len(notas)