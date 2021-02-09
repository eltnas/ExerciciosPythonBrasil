nomeAtleta = True
numAtleta = 0

while numAtleta != '' or nomeAtleta != '':
    numSalto = []
    numAtleta = int(input("Numero do Atleta: "))
    nomeAtleta = input("Nome do atleta: ")
    if numAtleta == '' or nomeAtleta == '':
        break
    else:
        salto = 1
        for i in range(5):
            distSalto = float(input("Distancia do {}° salto: ".format(salto)))
            numSalto.append(distSalto)
            salto += 1

        print("Nome do Atleta: {}".format(nomeAtleta))
        salto = 1
        cont = 0
        for i in range(5):
            print("{}° salto: {}m".format(salto,numSalto[cont]))
            salto += 1
            cont += 1
        
        print("Melhor Salto: {}m".format(max(numSalto)))
        print("Pior salto: {}m".format(min(numSalto)))

        numSalto.remove(max(numSalto))
        numSalto.remove(min(numSalto))
        mediaSalto = sum(numSalto) / len(numSalto)
        print("Media dos outros saltos: {}m".format(round(mediaSalto, 2)))
        print("\nResultado")
        print("Atleta: {} teve uma media de {}m!".format(nomeAtleta,round(mediaSalto, 2)))