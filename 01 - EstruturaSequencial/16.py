metro = float(input("Area em m2 a ser pintada: "))
litro = metro / 3

precoLitro = 80
capacidadeLitro = 18

latas = litro / capacidadeLitro
total = latas * precoLitro

print("Você precisará de ", latas,"latas de tinta")
print("O valor será de R$ ", total)