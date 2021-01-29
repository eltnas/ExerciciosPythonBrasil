def main():

	num1 = int(input("Valor 1: "))
	num2 = int(input("Valor 2: "))

	print("Qual operação vc quer fazer?")
	option = int(input("1 - Soma | 2 - Subtração | 3 - Multiplicação | 4 - Divisão :  "))

	if option == 1:
		result = num1 + num2
	elif option == 2:
		result = num1 - num2
	elif option == 3:
		result = num1 * num2
	elif option == 4:
		result = num1 / num2
	else:
		print("Opção inválida!")
		exit()

	print("O resultado é: ", result)

	if result%2 == 0:
		print("Numero par!")
	else:
		print("Numero Impar!")

	if result >= 0:
		print("Positivo")
	else:
		print("Negativo")


if __name__ == '__main__':
	main()