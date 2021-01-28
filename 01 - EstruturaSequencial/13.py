print("Dev: Elton C. Nascimento")
print("Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:")
print("a. Para homens: (72.7*h) - 58")
print("b. Para mulheres: (62.1*h) - 44.7")
print("--------------------------------------------")

alt = float(input("Qual a sua altura: "))
pesoH = (72.7 * alt) - 58
pesoM = (62.1 * alt) - 44.7

print("O peso ideal é:")
print("para um homem: ", pesoH,"kg")
print("para uma mulher: ", pesoM,"kg")