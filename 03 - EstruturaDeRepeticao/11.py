num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
soma = 0

for c in range(num1, num2+1):
	print(c)
	soma += c 

print("A soma de todos esses numeros é: {}".format(soma))