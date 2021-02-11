saltoEstenso = ['Primeiro','Segundo','Terceiro','Quarto','Quinto']
saltoAtleta = []
nomeAtleta = ''
esporte = True

while esporte == True:
    nome = str(input('Nome do atleta: '))
    if nome != '':
        for i in range(len(saltoEstenso)):
            salto = float(input(saltoEstenso[i] + " salto: "))
            saltoAtleta.append(salto)
            nomeAtleta = nome
    else:
        print('\n')
        print("=" *60)
        print('Atleta: ', nomeAtleta,'\n')
        for i in range(len(saltoEstenso)):
            print("{} salto: {} m2".format(saltoEstenso[i],saltoAtleta[i]))

        mediaSalto = sum(saltoAtleta) / 5
        print('\n')
        print('Resultado final')
        print('Atleta:              {}'.format(nomeAtleta))
        print('Saltos:              {}'.format(saltoAtleta))
        print('Media dos Saltos:    {}'.format(mediaSalto, 2))
        print('\n' *2, "Muito Obrigado!")
        break