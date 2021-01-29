print("Dev: Elton C. Nascimento")
print("-------------------------------------")

preco1 = float(input("Preço do primeiro produto: R$ "))
preco2 = float(input("Preço do segundo produto: R$ "))
preco3 = float(input("Preço do terceiro produto: R$ "))

if preco1 < preco2 and preco1 < preco3:
	print("Compre o produto 1!")
elif preco2 < preco1 and preco2 < preco3:
	print("Compre o produto 2!")
elif preco3 < preco1 and preco3 < preco2:
	print("Compre o produto 3!")
else:
	print("Não compre nenhum!")