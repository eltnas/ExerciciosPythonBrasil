num = float(input("Valor: "))

print(num, type(num))

def valorNum(v):
	n = int(v)
	m = v * 10
	s = n * 10

	if m == s :
		return ("O numero {} é inteiro".format(v))
	else:
		return("o numero {} é decimal".format(v))

r = valorNum(num)
print(r)