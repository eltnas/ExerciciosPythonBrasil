cand1 = str(input('Nome do candidato: ').upper())
voto1 = 0
cand2 = str(input('Nome do candidato: ').upper())
voto2 = 0
cand3 = str(input('Nome do candidato: ').upper())
voto3 = 0
qtdEleitor = int(input('Quantidade de eleitores: '))
eleitor = 0
maisVotos = []

while eleitor < qtdEleitor:
    print('Em quem você deseja votar?')
    print('01 - {}'.format(cand1))
    print('02 - {}'.format(cand2))
    print('03 - {}'.format(cand3))
    print(' ')
    voto = int(input('Digite seu voto (1/2/3): '))
    eleitor += 1

    if voto == 1:
        print('Seu voto foi para {}'.format(cand1))
        voto1 += 1
    elif voto == 2:
        print('Seu voto foi para {}'.format(cand2))
        voto2 += 1
    elif voto == 3:
        print('Seu voto foi para {}'.format(cand3))
        voto3 += 1
    else:
        print('Opção invalida!')
        eleitor = eleitor - 1

print('O candidato {} recebeu o total de {} votos'.format(cand1,voto1))
print('O candidato {} recebeu o total de {} votos'.format(cand2,voto2))
print('O candidato {} recebeu o total de {} votos'.format(cand3,voto3))
