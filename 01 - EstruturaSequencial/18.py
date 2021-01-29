tamanhoMb = float(input("Tamanho do arquivo a ser baixado (em mb): "))
valocidadeMb = float(input("Velocidade da internet a ser usada (em mb): "))

tempoDown = (tamanhoMb / valocidadeMb) * 60

print("O tempo estimado é de ", tempoDown,"minutos")