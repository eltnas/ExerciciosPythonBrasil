mult = int(input('Multiplicador: '))
numInicio = int(input('iniciar em   :'))
numFinal = int(input('Encerrar em  :'))

cont = numInicio

for i in range(numInicio, numFinal + 1):
    tab = mult * cont
    print('{} X {}: {}'.format(mult,cont,tab))
    cont += 1