nota = float(input("Insira uma nota de 1 - 10: "))

while (nota < 1) or (nota > 10):
	print("Valor invalido, tente novamente!")
	nota = float(input("Insira uma nota de 1 - 10: "))