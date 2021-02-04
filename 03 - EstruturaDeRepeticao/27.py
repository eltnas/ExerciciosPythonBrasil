qtdTurma = int(input('Quantas turmas: '))
alunosTurma = []
turma = 1

for i in range(qtdTurma):
    print('Turma {}'.format(turma))
    qtdAlunos = int(input('Quantidade de alunos: '))

turma += 1
alunosTurma.append(qtdAlunos)

mediaAlunos = sum(alunosTurma) / len(alunosTurma)
print('A media de alunos é de {} por sala!'.format(mediaAlunos))
