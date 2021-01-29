nota1 = float(input("insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota : "))

media = (nota1 + nota2) / 2

if media <= 3.9:
	print("Sua nota é E! Voce foi REPROVADO!")
elif media >= 4.0 and media <= 5.9:
	print("Sua nota é D! Voce foi REPROVADO!")
elif media >= 6.0 and media <= 7.4:
	print("Sua nota é C! Voce foi APROVADO! (Por pouco heim!)")
elif media >= 7.5 and media <= 8.9:
	print("Sua nota é B! Voce foi APROVADO!")
elif media >= 9.0:
	print("Sua nota é A! Voce foi APROVADO!")
