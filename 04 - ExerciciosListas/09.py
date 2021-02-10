quadrado = []
x = 1
while x <= 10:
    num = int(input("Digite o numero: "))
    mult = num * num
    quadrado.append(mult)
    x += 1

print("A soma do quadrado dos numeros é ", sum(quadrado))