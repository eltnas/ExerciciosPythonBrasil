# -*- coding: utf-8 -*-

numAlunos = []
altAlunos = []

for i in range(10):
    print("{}° Aluno".format(i + 1))
    nAluno = int(input("Codigo do Aluno: "))
    while nAluno in numAlunos:
        print("O codigo {} ja foi usado!!!".format(nAluno))
        nAluno = int(input("Digite outro Codigo: "))
    aAluno = altAlunos.append(float(input("Digite a altura do aluno: ")))
    numAlunos.append(nAluno)

indice_baixo = altAlunos.index(min(altAlunos))
indice_alto = altAlunos.index(max(altAlunos))

print("Aluno mais baixo \nNúmero: ", numAlunos[indice_baixo], "\nAltura: ", min(altAlunos))
print("Aluno mais alto \nNúmero: ", numAlunos[indice_alto], "\nAltura: ", max(altAlunos))