salAtual = float(input("Salario atual: R$ "))

aum5 = (salAtual / 100) * 5
aum10 = (salAtual / 100) * 10
aum15 = (salAtual / 100) * 15
aum20 = (salAtual / 100) * 20

if salAtual >= 1500:
	aumSal = salAtual + aum5
	print("Seu salario atual é de R$", salAtual)
	print("Voce receberá um aumento de 5%")
	print("Valor do aumento R$", aum5)
	print("Valor do salario com aumento R$", aumSal)

elif salAtual < 1500 and salAtual >= 700:
	aumSal = salAtual + aum10
	print("Seu salario atual é de R$", salAtual)
	print("Voce receberá um aumento de 10%")
	print("Valor do aumento R$", aum10)
	print("Valor do salario com aumento R$", aumSal)

elif salAtual < 700 and salAtual >= 280:
	aumSal = salAtual + aum15
	print("Seu salario atual é de R$", salAtual)
	print("Voce receberá um aumento de 15%")
	print("Valor do aumento R$", aum15)
	print("Valor do salario com aumento R$", aumSal)

elif salAtual < 280:
	aumSal = salAtual + aum20
	print("Seu salario atual é de R$", salAtual)
	print("Voce receberá um aumento de 20%")
	print("Valor do aumento R$", aum20)
	print("Valor do salario com aumento R$", aumSal)