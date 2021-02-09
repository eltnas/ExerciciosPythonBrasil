votoNum = [1,2,3,4,5,6]
votoCandidato = ['João','Jose','Paulo','Andre','Voto Nulo','Voto em Branco']
qtdVotos = 0
votar = []
votos = True

while votos != 0:
    print("Urna Eletronica - O sistema mais seguro que existe (dizem!)")
    print("=" *60)
    print("1 - João         | 2 - Jose")
    print("3 - Paulo        | 4 - Andre")
    print("5 - Voto Nulo    | 6 - Voto em Branco")
    print("\n")
    votos = int(input("Digite seu voto: "))
    if votos == 0:
        break
    else:
        while votos not in votoNum:
            print('Esse candidato nâo existe!')
            print("\n")
            print("1 - João         | 2 - Jose")
            print("3 - Paulo        | 4 - Andre")
            print("5 - Voto Nulo    | 6 - Voto em Branco")
            print("\n")
            votos = int(input("Digite seu voto: "))
        votar.append(votos)
    qtdVotos += 1

cont = 0
print("=" *60)
print("\n" *2)

print("Foram contados {} votos validos, e entre esses votos:".format(qtdVotos))
for i in range(len(votoCandidato)):
    if votar.count == 0:
        print("O candidato ",votoCandidato[cont], "não teve nenhum voto! ")
        cont += 1
    else:
        print("O candidato ",votoCandidato[cont], "teve um total de ", votar.count(cont + 1)," Votos")
        cont += 1

porcNulo = (votar.count(5) / len(votar)) * 100
porcBranco = (votar.count(6) / len(votar)) * 100
print("Voto Nulo totalizou ", votar.count(5),", o que totaliza a {}'%' dos votos!".format(porcNulo))
print("Voto em Branco totalizou ", votar.count(6),", o que totaliza {}'%' dos votos!".format(porcBranco))