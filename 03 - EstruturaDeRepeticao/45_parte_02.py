respCerta = []
respAluno = []
notaAluno = []

continuar = True

print("Parte do professor!!")
for i in range(10):
    gabarito = respCerta.append(input("Resposta da pergunta {}:".format(i+1)).upper())
numAluno = 1
while continuar != 'N':
    print("{}° aluno".format(numAluno))
    respAluno.clear()
    for i in range(10):
        resposta_aluno = respAluno.append(input("Resposta da pergunta {}: ".format(i+1)).upper())
    nota = 0
    for i in range(10):
        if respAluno[i] == respCerta[i]:
            nota += 1
    notaAluno.append(nota)
    continuar = input("Outro aluno vai responder? [s/n] : ").upper()
    numAluno += 1
print(len(notaAluno), "alunos responderam")
print("A maior nota foi: ", max(notaAluno))
print("A menor nota  foi: ", min(notaAluno))
print("A media de notas é de:", sum(notaAluno) / len(notaAluno))