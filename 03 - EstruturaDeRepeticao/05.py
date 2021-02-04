paisA = int(input("Insira a população do pais A: "))
taxaA = float(input("Qual a taxa de crescimento do pais A: "))
paisB = int(input("Insira a população do pais B: "))
taxaB = float(input("Qual a taxa de crescimento do pais B: "))
anos = 0

porceA = taxaA / 100
porceB = taxaB / 100

if paisA < paisB:
	while (paisA < paisB):
		anos += 1
		paisA = paisA + (paisA * porceA)
		paisB = paisB + (paisB * porceB)
	else:
		print("Apos ",int(anos),"anos o pais A ultrapassou o pais B com uma população de ", int(paisA)," enquato o pais B tem ",int(paisB))
else:
	while (paisA > paisB):
		anos += 1
		paisA = paisA + (paisA * porceA)
		paisB = paisB + (paisB * porceB)
	else:
		print("Apos ",int(anos),"anos o pais B ultrapassou o pais A com uma população de ", int(paisB)," enquato o pais B tem ",int(paisA))