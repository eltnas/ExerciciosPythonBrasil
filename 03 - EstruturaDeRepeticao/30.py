preco = float(input('Valor do pão: '))
cont = 1

while cont < 51:
    valor = cont * preco
    print('{} - R$ {}'.format(cont,valor))
    cont += 1