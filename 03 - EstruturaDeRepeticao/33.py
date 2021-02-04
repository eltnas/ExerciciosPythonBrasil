qtdTemperatura = int(input('Quantidade de Temperaturas: '))
temp = []
numTemperatura = 1
for i in range(qtdTemperatura):
    print('{}° temperatura'.format(numTemperatura))
    temperatura = temp.append(float(input('Valor: ')))
    numTemperatura += 1

print('Mais quente       : ', max(temp))
print('Mais frio         : ', min(temp))
print('Temperatura Media : ', round(sum(temp) / len(temp), 2))