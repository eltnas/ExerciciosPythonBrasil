par = 0
impar = 0

for n in range(0, 10):
	num = int(input('Digite um numero aleatorio: '))

	if num% 2 == 0:
		par += 1
	else:
		impar += 1

print('A quantidade de numeros pares são: {}, e impares são: {}'.format(par,impar))
