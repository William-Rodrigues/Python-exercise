"""Enunciado: Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes. 
Por essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos, 
solicitou que você criasse um sistema capaz de atender ao seguinte requisito: 
o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) 
e depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50). 
O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.

Há ainda um pedido especial do mantenedor: para que os professores não se confundam, 
ao digitar cada uma das notas deve ser exibida uma mensagem no seguinte padrão:
VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).
POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x."""


#TotalAlunos = int(50)
AlunosImpares = []
AlunosPares = []
TotalImpar = []
TotalPar = []

for TotalAlunos in range(1,50):
    if TotalAlunos % 2 != 0:
        AlunosImpares.append(TotalAlunos)
    else:
        AlunosPares.append(TotalAlunos)

print("VOCÊ ESTÁ DIGITANDO A NOTA DOS ALUNOS DE NÚMEROS ÍMPARES:")
for AlunosImpares in range(1,50,2):
    NotasImpar = float(input(f"Por favor insira a nota do aluno de número {AlunosImpares}:"))
    TotalImpar.append(NotasImpar)

print("VOCÊ ESTÁ DIGITANDO A NOTA DOS ALUNOS DE NÚMEROS PARES:")
for AlunosPares in range(2,51,2):
    NotasPar = float(input(f"Por favor insira a nota do aluno de número {AlunosPares}:"))
    TotalPar.append(NotasPar)

SomaImpar = sum(TotalImpar)
SomaPar = sum(TotalPar)

MediaTurmaImpar = SomaImpar / 25
MediaTurmaPar = SomaPar / 25

if MediaTurmaImpar > MediaTurmaPar:
    print(f"Média da turma Ímpar: {MediaTurmaImpar}")
    print(f"Média da turma Par: {MediaTurmaPar}")
    print(f"A Média dos alunos Ímpar foi maior que da turma par: {MediaTurmaImpar}")
elif MediaTurmaPar > MediaTurmaImpar:
    print(f"Média da turma Par: {MediaTurmaPar}")
    print(f"Média da turma Ímpar: {MediaTurmaImpar}")
    print(f"A Média dos alunos Par foi maior que da turma ímpar: {MediaTurmaPar}")
elif MediaTurmaImpar == MediaTurmaPar:
    print(f"Média da turma Par: {MediaTurmaPar}")
    print(f"Média da turma Ímpar: {MediaTurmaImpar}")
    print(f"Houve um empate entre a média das turmas Par e Ímpar")