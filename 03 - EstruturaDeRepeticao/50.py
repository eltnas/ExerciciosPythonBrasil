h = 1
n = 2
listaH = []
listaN = []
print("H = 1 +", end = "")
while n <= 10 -1:
    print(" ",h, "/", n, " + ", end="")
    listaH.append(h)
    listaN.append(n)
    n += 1
print(h, "/", n, " = ", sum(listaH), "/", sum(listaN), " = ", round(sum(listaH) / sum(listaN)), 2)