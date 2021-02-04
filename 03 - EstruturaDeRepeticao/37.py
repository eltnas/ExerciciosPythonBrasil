codCliente = []
altCliente = []
pesoCliente = []
numCliente = 1
codigo = True

while codigo != 0:
    print('Cliente n°: {}'.format(numCliente))
    codigo = int(input('Codigo Cliente: '))
    if codigo == 0:
        break
    else:
        altura = float(input('Altura: '))
        peso = float(input('Peso: '))
        codCliente.append(codigo)
        altCliente.append(altura)
        pesoCliente.append(peso)
        numCliente += 1

cod_magro = pesoCliente.index(min(pesoCliente))
cod_gordo = pesoCliente.index(max(pesoCliente))
cod_alto = altCliente.index(max(altCliente))
cod_baixo = altCliente.index(min(altCliente))
print('-' * 20)
print('Mais magro  : ', codCliente[cod_magro])
print('Mais Gordo  : ', codCliente[cod_gordo])
print('Mais Alto   :', codCliente[cod_alto])
print('Mais Baixo  :', codCliente[cod_baixo])
print('Altura Média: ', sum(altCliente) / len(altCliente))
print('Peso Médio  : ', sum(pesoCliente) / len(pesoCliente))