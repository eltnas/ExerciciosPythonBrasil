#41 - Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
#Os juros e a quantidade de parcelas seguem a tabela abaixo:
#	Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
#		1       0
#		3       10
#		6       15
#		9       20
#		12      25
#	Exemplo de saída do programa:
#	Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
#		R$ 1.000,00     0               1                       R$  1.000,00
#		R$ 1.100,00     100             3                       R$    366,00
#		R$ 1.150,00     150             6                       R$    191,67

valorDivida = float(input("Digite o valor da divida: R$ "))
qtdParcela = 1
print("\n" * 2)
print("Valor da divida: ", end=" | ")
print("Valor do juros: ", end=" | ")
print("Qtd parcelas: ", end=" | ")
print("Valor da parcela: ")

for i in range(5):
    if qtdParcela == 1:
        juros = 1
        valorJuros = 0
    elif qtdParcela == 4:
        qtdParcela = 3
        juros = 1.10
    elif qtdParcela == 7 or qtdParcela == 6:
        qtdParcela = 6
        juros = 1.15
    elif qtdParcela == 10 or qtdParcela == 9:
        qtdParcela = 9
        juros = 1.20
    elif qtdParcela == 13 or qtdParcela == 12:
        qtdParcela = 12
        juros = 1.25

    valorJuros = valorDivida * (juros - 1)
    jurosDivida = valorDivida * juros
    valorParcela = jurosDivida / qtdParcela

    print("R$", round(jurosDivida, 2), end="       |       ")
    print(round(valorJuros, 2), end="       |       ")
    print(qtdParcela, end="       |       ")
    print("R$ ", round(valorParcela, 2))
    qtdParcela += 3