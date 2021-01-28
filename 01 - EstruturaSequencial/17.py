print("Dev: Elton C. Nascimento")
print("Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.")
print("Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:")
print("a. comprar apenas latas de 18 litros;")
print("b. comprar apenas galões de 3,6 litros;")
print("c. misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.")
print("-------------------------------------------------")

import math

m2 = float(input("Informe a area que será pintada: "))
consLitro = m2 / 6
print("\no consumo de tinta é: {:.2f} Litros\n".format(consLitro))

latas18 = consLitro / 18
latas36 = consLitro / 3.6

print("A quantidade de latas de 18 lt a serem usados é: {}".format(math.ceil(latas18)))
print("A quantidade de latas de 3.6 lt a serem usadas é: {}\n".format(math.ceil(latas36)))

print("Verificando o disperdicio de tintas")

dispLatas18 = ((consLitro * 0.1) + consLitro) / 18
litros18 = math.trunc(dispLatas18) * 18
resto18 = ((consLitro * 0.1) + consLitro) - litros18

dispLatas36 = resto18 / 3.6
dispLatasTotal = math.trunc(dispLatas18) + math.ceil(dispLatas36)
valorLata18 = math.trunc(dispLatas18) * 80
valorLata36 = math.ceil(dispLatas36) * 25
valorTotal = valorLata18 + valorLata36

print("Quantidades de latas de 18 lt é: {}".format(math.trunc(dispLatas18)))
print("Quantidades de latas de 3.6 lt é: {}".format(math.ceil(dispLatas36)))
print("Valor total a ser gasto é: R$ {}".format(valorTotal))