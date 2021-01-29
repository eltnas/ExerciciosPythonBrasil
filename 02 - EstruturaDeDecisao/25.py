respSim = 0
perg = str(input("Telefonou para a vítima? ").lower())
if perg == 'sim' or perg == 's':
	respSim = respSim + 1 

perg = str(input("Esteve no local do crime? ").lower())
if perg == 'sim' or perg == 's':
	respSim = respSim + 1 

perg = str(input("Mora perto da vítima? ").lower())
if perg == 'sim' or perg == 's':
	respSim = respSim + 1 

perg = str(input("Devia para a vítima? ").lower())
if perg == 'sim' or perg == 's':
	respSim = respSim + 1 

perg = str(input("Já trabalhou com a vítima? ").lower())
if perg == 'sim' or perg == 's':
	respSim = respSim + 1 
	
if respSim == 2:
	print("Suspeito(a)")
elif respSim == 3 or respSim == 4:
	print("Cúmplice")
elif respSim == 5:
	print("Assassino(a)")
else:
	print("Inocente")