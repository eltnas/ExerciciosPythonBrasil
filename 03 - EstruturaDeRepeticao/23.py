num = int(input('Numero: '))
lista = []
div = 0

for i in range(num + 1):
    if i % 2 == 1 and i != 2:
        lista.append(i)
        div += 1
    else:
        div += 1
print('Numeros primos: {}'.format(lista))
print('Numero de divisoes: {}'.format(div))