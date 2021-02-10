vetorA = []
vetorB = []
x = 1
y = 1

print("Vetor A")
while x <= 10:
    num = int(input("Digite o numero: "))
    vetorA.append(num)
    x += 1

print("Vetor B")
while y <= 10:
    num = int(input("Digite o numero: "))
    vetorB.append(num)
    y += 1

print(*sum(zip(vetorA,vetorB),()))