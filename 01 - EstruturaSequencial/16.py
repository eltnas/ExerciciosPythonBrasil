
print("Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.")

metro = float(input("Area em m2 a ser pintada: "))
litro = metro / 3

precoLitro = 80
capacidadeLitro = 18

latas = litro / capacidadeLitro
total = latas * precoLitro

print("Você precisará de ", latas,"latas de tinta")
print("O valor será de R$ ", total)