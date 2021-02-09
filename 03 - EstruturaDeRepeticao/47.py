nomeAtleta = True
numAtleta = 0

while nomeAtleta != '':
    notaJurado = []
    nomeAtleta = input("Nome do atleta: ")
    if nomeAtleta == '':
        break
    else:
        nota = 1
        for i in range(7):
            jurNota = float(input("{}° jurado: ".format(nota)))
            notaJurado.append(jurNota)
            nota += 1

        print("Nome do Atleta: {}".format(nomeAtleta))
        nota = 1
        cont = 0
        for i in range(5):
            print("{}° nota: {}".format(nota,notaJurado[cont]))
            nota += 1
            cont += 1
        
        print("Melhor nota: {}".format(max(notaJurado)))
        print("Pior nota: {}".format(min(notaJurado)))

        notaJurado.remove(max(notaJurado))
        notaJurado.remove(min(notaJurado))
        mediaNota = sum(notaJurado) / len(notaJurado)
        print("Media das notas: {}".format(round(mediaNota, 2)))
        print("\nResultado")
        print("Atleta: {} teve uma media de {}!".format(nomeAtleta,round(mediaNota, 2)))