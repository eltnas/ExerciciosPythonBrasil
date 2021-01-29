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