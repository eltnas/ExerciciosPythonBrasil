notasLista = []
numero = 0
cont1 = 0
cont2 = 0

while numero >= 0:
    numero = float(input("Numero: "))
    notasLista.append(numero)
    
else:
    print('=' *50)
    notasLista.remove(-1.0)
    print('a) Mostre a quantidade de valores que foram lidos;\n',len(notasLista))
    print('b) Exiba todos os valores na ordem em que foram informados, um ao lado do outro;\n',notasLista)
    print('=' *50)

    print('c) Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;\n')
    for i in range(0, len(notasLista)):
        listaReversa = notasLista[::-1]
        print(listaReversa[i])
        somaLista = sum(notasLista)
        mediaLista = somaLista / len(notasLista)

        if notasLista[i] > mediaLista:
            cont1 += 1

        if notasLista[i] < 7:
            cont2 += 1
    
    print('=' *50)
    print('d) Calcule e mostre a soma dos valores;\n',somaLista,'\n')
    print('e) Calcule e mostre a média dos valores;\n',mediaLista,'\n')
    print('f) Calcule e mostre a quantidade de valores acima da média calculada;\n', cont1,'\n')
    print('g) Calcule e mostre a quantidade de valores abaixo de sete;\n',cont2)

    print('h) Encerre o programa com uma mensagem;')
    print('-=' *25)
    print('\n')
    print('Muito Obrigado!!!!!!!\n\n')

