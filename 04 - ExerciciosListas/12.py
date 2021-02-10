#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

iddAluno = []
altAluno = []
x = 0
cont = 0
altMedia = 0

for i in range(30):
    idade = int(input("Idade do aluno: "))
    altura = float(input("Altura do aluno: "))
    iddAluno.append(idade)
    altAluno.append(altura)
    Media = sum(altAluno) / len(altAluno)
    altMedia = Media

for j in range(len(altAluno)):    
    if iddAluno[j] >= 13:
        if altAluno[j] > altMedia:
            cont += 1

print("Tem {} alunos acima de 13 anos com altura maior que a media da sala de {}".format(cont, altMedia))