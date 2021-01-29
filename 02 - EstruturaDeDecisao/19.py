num = int(input("Insira o numero: "))

uni = num % 10
dez = ((num - uni) / 10) % 10
cen = ((num - uni - (dez * 10)) / 100) % 10

print("O numero informado tem ", cen, "centena(s), ", dez, " dezena(s) e ", uni, " unidade(s)")