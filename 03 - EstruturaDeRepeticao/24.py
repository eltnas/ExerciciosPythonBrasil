qtd = int(input('Quantas notas: '))
count = 0
notas = []

while count < qtd:
    notas2 = notas.append(float(input('Nota: ')))
    count += 1

media = sum(notas) / qtd
print('A media é {}'.format(media))