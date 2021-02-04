nome = str(input("informe um nome: "))
while (len(nome) <=  3 ):
	print("Voce precisa informar seu nome!")
	nome=str(input("informe um nome: "))

idade = int(input("Qual a sua idade: "))
while (idade < 0 or idade > 150 ):
	print("Voce não parece ter essa idade! Tente novamente!")
	idade = int(input("Qual a sua idade: "))

salario = float(input("Qual seu salario: "))
while (salario < 0):
	print("Conta qual é o seu salario!")
	salario = float(input("Qual seu salario: "))

sexo = str(input("Qual seu sexo (h - Homem, m - Mulher): ").upper())
while sexo != "H" and sexo != "M":
	print("Voce precisa nos dizer seu sexo!")
	sexo = str(input("Qual seu sexo (h - Homem, m - Mulher): ").upper())

estCivil = str(input("Qual seu estado Civil (s - Solteiro, c - Casado, v - Viuvo ou d - Divorciado: ").upper())
while (estCivil != 'S' and estCivil != 'C' and estCivil != 'V' and estCivil != 'D'):
	print("Por favor, nos informe seu estado civil!")
	estCivil = str(input("Qual seu estado Civil (s - Solteiro, c - Casado, v - Viuvo ou d - Divorciado: ").upper())