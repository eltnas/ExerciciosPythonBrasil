selFruta = int(input("Você deseja comprar Morango(1) ou Maçã(2)? "))

if selFruta == 1:
	selKilo = float(input("Quantos kilos você deseja? "))

	if selKilo > 5:
		preco = 2.20
		precoTotal = selKilo * preco
		if selKilo >= 8 or precoTotal >= 25.00:
			desc = (precoTotal / 100) * 10
			valor = precoTotal - desc
			print("O valor a ser pago é R$",valor)
		else:
			valor = precoTotal
			print("O valor a ser pago é de R$",valor)
	else:
		preco = 2.50
		precoTotal = selKilo * preco

		valor = precoTotal
		print("O valor a ser pago é de R$",valor)

elif selFruta == 2:
	if selKilo > 5:
		preco = 2.20
		precoTotal = selKilo * preco
		if selKilo >= 8 or precoTotal >= 25.00:
			desc = (precoTotal / 100) * 10
			valor = precoTotal - desc
			print("O valor a ser pago é R$",valor)
		else:
			valor = precoTotal
			print("O valor a ser pago é de R$",valor)
	else:
		preco = 2.50
		precoTotal = selKilo * preco

		valor = precoTotal
		print("O valor a ser pago é de R$",valor)
else:
	print("Opção invalida!!")
