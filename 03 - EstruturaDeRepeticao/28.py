qtdCds = int(input('Quantidade de CDs: '))
cds = []
numCd = 1

for i in range(qtdCds):
    print('CD: {}'.format(numCd))
    valorCd = cds.append(float(input('Valor: ')))
    numCd += 1

media = sum(cds) / len(cds)
print('O valor medio de cada CD é R${}'.format(media))