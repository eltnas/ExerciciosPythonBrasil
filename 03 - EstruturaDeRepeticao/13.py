base = int(input("Base: "))
expo = int(input("Expoente: "))
res = 1

for c in range(expo):
	res *= base
	c += 1

print('O resultado é: {}^{} = {}'.format(base, expo, res))