lista = []
cont = 1

while cont <= 5:
    num = int(input("Numero: "))
    cont += 1
    lista.append(num)

print("Os numeros digitados foi: ", lista)

soma = sum(lista)
print("Se somar todos: ", soma)

multi = 1
for x in lista:
    multi *= x
print("Se multiplica-los: ", multi)
