import math
num = int(input('Numero: '))
cont = num
fat = math.factorial(num)

for i in range(num - 1):
    print(cont, end=" * ")
    cont -= 1
print("1 = ", fat)