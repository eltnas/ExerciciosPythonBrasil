pesoPeixe = float(input("Insira o peso do peixe: "))

if pesoPeixe > 50:
	pesoExcesso = pesoPeixe - 50
	multaPeso = (pesoPeixe - 50) * 4
	print("O peso do peixe está acima do permitido, você pagará uma multa de R$ ", multaPeso)
else:
	print("O peixe está no peso permitido")
