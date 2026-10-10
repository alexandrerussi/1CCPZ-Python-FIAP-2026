from aluno import Aluno # PascalCase
from disciplina import Disciplina

# criar / instanciar 1 aluno
aluno1 = Aluno("João", "123456", "Ciência da Computação")
# print(aluno1.notas_por_disciplina)

# criar / instanciar 2 disciplinas
cs = Disciplina("Computer Science", "Lucas")
dsa = Disciplina("Data Structure", "Álvaro")
# print(dsa.professor)
# dsa.exibir_infos()

# matricular o aluno1 nas 2 disciplinas
aluno1.matricular(cs)
aluno1.matricular(dsa)
# print(aluno1.disciplinas[1].professor)

aluno1.adicionar_nota(cs, 10)
aluno1.adicionar_nota(cs, 8)
aluno1.adicionar_nota(dsa, 5)
aluno1.adicionar_nota(dsa, 3)
# print(aluno1.notas_por_disciplina)

print(aluno1.calcular_media_d(dsa))