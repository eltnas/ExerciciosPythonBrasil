num = int(input("Numero: "))
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0

num2 = num
while num2 <= 100 and num2 >= 76:
    cont4 = cont4 + 1
    num2 = num2 - 1
while num2 <= 75 and num2 >= 51:
    cont3 = cont3 + 1
    num2 = num2 - 1
while num2 <= 50 and num2 >= 26:
    cont2 = cont2 + 1
    num2 = num2 - 1
while num2 <= 25 and num2 >= 0:
    cont1 = cont1 + 1
    num2 = num2 - 1

print("O numero informado foi: {}".format(num))
print("Existem {} numeros positivos entre 0 e 25!".format(cont1))
print("Existem {} numeros positivos entre 26 e 50!".format(cont2))
print("Existem {} numeros positivos entre 51 e 75!".format(cont3))
print("Existem {} numeros positivos entre 76 e 100!".format(cont4))
