vetorA = []
vetorB = []
vetorC = []
x = 1
y = 1

print("Vetor A")
for i in range(10):
    num = int(input("Digite o numero: "))
    vetorA.append(num)

print("Vetor B")
for i in range(10):
    num = int(input("Digite o numero: "))
    vetorB.append(num)

print("Vetor C")
for i in range(10):
    num = int(input("Digite o numero: "))
    vetorC.append(num)

print(*sum(zip(vetorA,vetorB,vetorC),()))