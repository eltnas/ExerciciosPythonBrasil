numAluno = []
notaAluno = []
cont = 0

contAluno = 1

while contAluno <= 10:
    numAluno = int(input("Numero do aluno: "))
    notaAluno = float(input("Nota do aluno: "))
    contAluno += 1
    if notaAluno >= 7.0:
        cont += 1

print("O numero de alunos com media igual ou superior a 7.0 é: %d" %cont)