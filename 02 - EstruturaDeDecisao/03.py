# -*- coding: latin-1 -*

sexo = str(input("Selecione o sexo (m/h): ").upper())

if sexo == 'M':
	print("O sexo selecionado é Mulher (m)!")
elif sexo == 'H':
	print("O sexo selecionado é Homem (h)!")
else:
	print("Sexo inválido!")