#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
num = []
numPar = 0
numImpar = 0
x = 1

while x <= 20:
    num = int(input("Numero: "))
    x += 1
    if num % 2 == 0:
        numPar += 1
    else:
        numImpar += 1

print("Foram inseridos {} numeros pares e {} numeros impares!".format(numPar,numImpar))

