nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segudna nota : "))
nota3 = float(input("Insira a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media == 10:
	print("Voce foi APROVADO COM DISTINÇÃO, com a nota ", media)
elif media >= 7 and media <= 9.9:
	print("Voce foi APROVADO, com a nota ", media)

elif media < 7:
	print("Voce foi REPROVADO, com a nota ", media)
