import math

a = int(input("Coeficiente de a: "))

if a == 0:
	print("Se a é igual a ZERO, não é uma equação de segundo grau! Até logo!")

else:
	b = int(input("Coeficiente de b: "))
	c = int(input("Coeficiente de c: "))

	delta = b*b - (4-a*c)

	if delta < 0:
		print("Delta menor que 0. Raizes imaginarias. Até logo!")

	elif delta == 0:
		raiz = -b / (2 * a)
		print("Delta = 0 raiz= ", raiz)

	else:
		raiz1 = (-b + math.sqrt(delta)) / (2 * a)
		raiz2 = (-b - math.sqrt(delta)) / (2 * a)

		print("Raizes: ", raiz1, " e ", raiz2)