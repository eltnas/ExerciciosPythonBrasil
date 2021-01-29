tipoCombustivel = str(input("Gasolina ou Alcool? (G/A)").upper())
qtdCombustivel = float(input("Quantos litros? "))

if tipoCombustivel == 'G':
	precoCombustivel = 2.50
	print("Gasolina litro: R$",precoCombustivel)

	if qtdCombustivel > 20:
		desc = ((qtdCombustivel * precoCombustivel) / 100) * 6
		preco = qtdCombustivel * precoCombustivel
		total = preco - desc
		print("Quantidade de litros abastecido :",qtdCombustivel,"lt")
		print("Valor por litro de Gasolina     : R$",precoCombustivel)
		print("Total                           : R$",preco)
		print("Valor do desconto ofertado      : R$",desc)
		print("O valor a ser pago é de         : R$",total)

	else:
		desc = ((qtdCombustivel * precoCombustivel) / 100) * 4
		preco = qtdCombustivel * precoCombustivel
		total = preco - desc
		print("Quantidade de litros abastecido :",qtdCombustivel,"lt")
		print("Valor por litro de Gasolina     : R$",precoCombustivel)
		print("Total                           : R$",preco)
		print("Valor do desconto ofertado      : R$",desc)
		print("O valor a ser pago é de         : R$",total)

elif tipoCombustivel == 'A':
	precoCombustivel = 1.90
	print("Alcool litro: R$",precoCombustivel)
	if qtdCombustivel > 20:
		desc = ((qtdCombustivel * precoCombustivel) / 100) * 5
		preco = qtdCombustivel * precoCombustivel
		total = preco - desc

		print("Quantidade de litros abastecido :",qtdCombustivel,"lt")
		print("Valor por litro de Alcool       : R$",precoCombustivel)
		print("Total                           : R$",preco)
		print("Valor do desconto ofertado      : R$",desc)
		print("O valor a ser pago é de         : R$",total)

	else:
		desc = ((qtdCombustivel * precoCombustivel) / 100) * 3
		preco = qtdCombustivel * precoCombustivel
		total = preco - desc

		print("Quantidade de litros abastecido :",qtdCombustivel,"lt")
		print("Valor por litro de Alcool       : R$",precoCombustivel)
		print("Total                           : R$",preco)
		print("Valor do desconto ofertado      : R$",desc)
		print("O valor a ser pago é de         : R$",total)


else:
	print("Essa opção não é valida!")
