dinheiro = int(input("Valor a ser sacado (10 - 600): "))

cem = int(dinheiro / 100)
dinheiro = dinheiro - (cem * 100)

cinquenta = int(dinheiro / 50)
dinheiro = dinheiro - (cinquenta * 50)

dez = int(dinheiro / 10)
dinheiro = dinheiro - (dez * 10)

cinco = int(dinheiro / 5)
dinheiro = dinheiro - (cinco * 5)

um = dinheiro

print("Será sacado essa quantidade de notas:")
print("notas de R$ 100: ", cem)
print("notas de R$ 50 : ", cinquenta)
print("notas de R$ 10 : ", dez)
print("notas de R$ 5  : ", cinco)
print("notas de R$ 1  : ", um)