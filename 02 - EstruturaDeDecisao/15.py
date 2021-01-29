ladoA = int(input("Insira o primeiro lado : "))
ladoB = int(input("Insira o segundo lado  : "))
ladoC = int(input("Insira o terceiro lado : "))

if ladoA == ladoB and ladoB == ladoC:
	print("Esse é um triangulo equilatero!")

elif ladoA != ladoB and ladoB != ladoC:
	print("Esse é um triangulo Escaleno!")

elif ladoA == ladoB or ladoB == ladoC:
	print("Esse é um Triângulo Isósceles")