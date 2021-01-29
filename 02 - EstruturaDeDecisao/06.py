num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
num3 = int(input("Numero 3: "))

if num1 > num2 and num1 > num3:
	print("O numero ", num1,"e o maior!")
elif num2 > num1 and num2 > num3:
	print("O numero ", num2, "e o maior!")
elif num3 > num1 and num3 > num2:
	print("O numero ", num3, "e o maior!")
else:
	print("Opcao invalida!")
