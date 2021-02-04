paisA = 80000
paisB = 200000
taxaA = 0.03
taxaB = 0.015
anos = 0

while (paisA < paisB):
	anos += 1
	paisA = paisA + (paisA * taxaA)
	paisB = paisB + (paisB * taxaB)
else:
	print("Apos ",int(anos),"anos o pais A ultrapassou o pais B com uma população de ", int(paisA)," enquato o pais B tem ",int(paisB))