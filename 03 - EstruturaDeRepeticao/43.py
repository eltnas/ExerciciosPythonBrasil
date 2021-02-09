cod = [100,101,102,103,104,105]
produtos = ['Cachorro Quente','Bauru Simples','Bauru com ovo','Hambúrguer','Cheeseburguer','Refrigerante']
valor = [1.20,1.30,1.50,1.20,1.30,1]
codigo = True
pedidoNum = 1
pedidos = []

while codigo != 0:
    print("{}° pedido.".format(pedidoNum))
    codigo = int(input("Codigo do produto: "))
    if codigo == 0:
        break
    else:
        while codigo not in cod:
            print("Esse produto não existe!")
            codigo = int(input("Codigo do produto: "))

        indice = cod.index(codigo)
        qtd = int(input("Quantidade: "))
        valorPedido = valor[indice] * qtd
        pedidos.append(valorPedido)
    pedidoNum += 1

anotaPedido = 0
print('\n')
for i in range(pedidoNum - 1):
    print(anotaPedido + 1,"° pedido: R$", round(pedidos[anotaPedido], 3))
    anotaPedido += 1
print("Total a pagar: R$", round(sum(pedidos), 3))
