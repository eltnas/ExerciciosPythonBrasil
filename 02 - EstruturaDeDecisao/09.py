num1 = int(input("Insira o primeiro numero: "))
num2 = int(input("Insira o segundo numero : "))
num3 = int(input("Insira o terceiro numero: "))

if num3 > num2:
	numAux = num3
	num3 = num2
	num2 = numAux

elif num2 > num1:
	numAux = num2
	num2 = num1
	num1 = numAux

elif num3 > num2:
	numAux = num3
	num3 = num2
	num2 = numAux

print("A sequencia é ", num1," - ", num2," - ", num3)