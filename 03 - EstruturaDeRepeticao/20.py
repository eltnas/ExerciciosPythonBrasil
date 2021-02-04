cond = True
qtd = int(input('Quantidade de vezes: '))
num = int(input('Numero: '))
fat = 1
res = 1

for i in range(0, qtd):
	while fat <= num:
		res *= fat
		fat += 1
	print('O fatorial do numero {} é: {}'.format(num,res))
	qtd = qtd - 1
	
