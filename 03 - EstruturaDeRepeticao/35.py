num = int(input('Digite o numero: '))
mult = 0
numLista = []

for cont in range(2, num):
    if num %cont == 0:
        mult += 1
        numLista.append(cont)

if mult != 0:
    print('Não é numero primo!')
    print('Numeros Primos entre 1 e {}: {}'.format(num,numLista))
else:
    print('Numero primo!')
    print('Numeros Primos entre 1 e {}: {}'.format(num,numLista))