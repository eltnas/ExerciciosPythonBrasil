soma = 0
media = 0

for c in range(0, 5):
	num = int(input("Informe um numero: "))
	soma += num
	media = soma / 5

print("A soma desses numero é: {}".format(soma))
print("A media entre eles é: {}".format(media))