# -*- coding: utf-8 -*-
import math
numCidade = 0
qtdVeiculos = 0
qtdAcidentes = 0
acidente2000 = 0
cont = 0
maiorAcidente = 0
menorAcidente = 0
maiorCidade = 0
menorCidade = 0

for c in range(5):
    print("{}° cidade".format(c + 1))
    codCidade = int(input("Digite o codigo da cidade: "))
    numVeiculo = int(input("Quantidade de veiculos: "))
    numAcidente = int(input("Quantidade de acidentes: "))

    qtdVeiculos += numVeiculo
    qtdAcidentes += numAcidente

    if numAcidente > maiorAcidente:
        maiorAcidente = numAcidente
        maiorCidade = codCidade

    if numAcidente < menorAcidente or c == 1:
        menorAcidente = numAcidente
        menorCidade = numCidade

    if numAcidente < 2000:
        acidente2000 += numAcidente
        cont += 1

mediaCidade = qtdVeiculos / c
media2000 = acidente2000 / cont

print("+=" * 30)
print("A media de veiculos de todas as cidades é de {} veiculos.".format(mediaCidade))
print("A cidade com o menor indice de acidentes é a {}, com um total de {} acidentes.".format(menorCidade,menorAcidente))
print("A cidade com o maior indice de acidentes é a {}, com um total de {} acidentes.".format(maiorCidade,maiorAcidente))
print("A media de acidentes nas cidades com menos de 2000 veiculos é de {} acidentes.".format(media2000))