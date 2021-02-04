num = int(input('Digite o numero: '))
mult = 0

for cont in range(2, num):
    if num %cont == 0:
        mult += 1

if mult != 0:
    print('Não é numero primo!')
else:
    print('Numero primo!')