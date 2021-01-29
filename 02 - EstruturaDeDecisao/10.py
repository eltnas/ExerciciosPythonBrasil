turno = str(input("Qual turno vc estuda? (M-Matutino, V-Vespertino, N-Noturno): ").upper())

if turno == 'M':
	print("Bom dia!")
elif turno == 'V':
	print("Boa tarde!")
elif turno == 'N':
	print("Boa noite!")
else:
	print("Valor Invalido!")