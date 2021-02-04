num = int(input("Numero: ") )
res = 1
cont = 1

while cont <= num:
    res *= cont
    cont += 1

print('O fatorial do numero {} é {}'.format(num, res))