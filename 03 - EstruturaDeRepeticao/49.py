num1 = 1
num2 = 1
lista1 = []
lista2 = []
print("S = ", end = "")
while num1 <= 10 -1:
    print(num1, "/", num2, " + ", end="")
    lista1.append(num1)
    lista2.append(num2)
    num1 += 1
    num2 += 2

print(num1, "/", num2, " = ", sum(lista1), "/", sum(lista2))