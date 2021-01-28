print("Dev: Elton C. Nascimento")
print("-------------------------------------")

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10:
	print("Aprovado com Distincao!!")
elif media <= 9.9 and media >= 7:
	print("Aprovado!")
else:
	print("Reprovado!")