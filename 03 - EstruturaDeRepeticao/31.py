#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
#	Lojas Tabajara 
#		Produto 1: R$ 2.20
#		Produto 2: R$ 5.80
#		Produto 3: R$ 0
#		Total: R$ 9.00
#		Dinheiro: R$ 20.00
#		Troco: R$ 11.00
#		...

prod1 = 'Requeijão'
valorProd1 = 5.90
contProd1 = 1

prod2 = 'Caneta'
valorProd2 = 1.9
contProd2 = 1

prod3 = 'Isqueiro'
valorProd3 = 10.9
contProd3 = 1

compra = int(input('Digite o codigo do produto: '))

while compra != 0:
    compra = int(input('Digite o codigo do produto: '))
    if compra == 1:
        contProd1 +=1
    elif compra == 2:
        contProd2 += 1
    elif compra == 3:
        contProd3 += 1
    elif compra == 0:
        print('======================================')
    else:
        print('Produto não existe!')
else:
    totalCompra = (contProd1 * valorProd1) + (contProd2 * valorProd1) + (contProd3 * valorProd1)
    print('Sua compra foi no total de : R$ {}'.format(totalCompra))
    valorPgt = float(input('Dinheiro: R$'))
    troco = valorPgt - totalCompra
    print('Foi pago R$ {} e precisa voltar R$ {}'.format(valorPgt,troco))