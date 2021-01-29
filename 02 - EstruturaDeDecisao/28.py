selCarne = int(input("File Duplo(1), Alcatra(2) ou Picanha(3)"))

if selCarne == 1:
	selKilo = float(input("Quantos kilos de File Duplo você quer? "))

	if selKilo < 5:
		carneValor = 4.90
	else: 
		carneValor = 5.80
elif selCarne == 2:
	selKilo = float(input("Quantos kilos de Alcatra você quer? "))

	if selKilo < 5:
		carneValor = 5.90
	else:
		carneValor = 6.80

elif selCarne == 3:
	selKilo = float(input("Quantos kilos de Picanha você quer? "))

	if selKilo < 5:
		carneValor = 6.90
	else:
		carneValor = 7.80

else:
	print("Opção invalida!")

ValorPagar = selKilo * carneValor

print("O valor a pagar é de R$",ValorPagar)
tipoPgt = str(input("Pagamento em Dinheiro(D), Cartão de Credito(C) ou Cartão Tabajara(T) ").upper())

if tipoPgt == 'T':
	desc = (ValorPagar / 100) * 5
	totalPagar = ValorPagar - desc
	print("Ao pagar com Cartão Tabajara você recebeu um desconto de R$",desc)
	print("--------------------------------------------------------------------")
	print("Valor total a pagar: R$",totalPagar)

elif tipoPgt == 'D' or tipoPgt == 'C':
	totalPagar = ValorPagar
	print("Valor total a pagar: R$",totalPagar)

else:
	print("Opção Invalida!")
