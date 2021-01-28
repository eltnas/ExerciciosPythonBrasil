print("Dev: Elton C. Nascimento")
print("Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)")
print("---------------------------------------------")

tamanhoMb = float(input("Tamanho do arquivo a ser baixado (em mb): "))
valocidadeMb = float(input("Velocidade da internet a ser usada (em mb): "))

tempoDown = (tamanhoMb / valocidadeMb) * 60

print("O tempo estimado é de ", tempoDown,"minutos")