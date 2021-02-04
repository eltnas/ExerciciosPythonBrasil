cond = True
soma = 0
num = []

while cond:
    num2 = int(input('Numero (0 - 1000): '))

    if (num2 > 0 and num2 < 1001):
        soma += num2
        num.append(num2)
    else:
        break

print('O numero {} é o menor'.format(min(num)))
print('O numero {} é o maior'.format(max(num)))
print('E a soma de todos eles é {}'.format(soma))
