respCertas = ['A','B','C','D','E','E','D','C','B','A']
respAluno = []
notaAluno = []
numAluno = 0
continuar = True

while continuar != 'N':
    print("{}° aluno".format(numAluno))
    respAluno.clear()
    for i in range(10):
        print("Questão: ", i + 1)
        resposta_aluno = respAluno.append(input("Resposta: ").upper())
    nota = 0
    for i in range(10):
        if respAluno[i] == respCertas[i]:
            nota += 1
    notaAluno.append(nota)
    continuar = input("Outro aluno vai responder? [s/n] : ").upper()
    numAluno += 1
print(len(notaAluno), "alunos responderam")
print("A maior nota foi: ", max(notaAluno))
print("A menor nota  foi: ", min(notaAluno))
print("A media de notas é de:", sum(notaAluno) / len(notaAluno))