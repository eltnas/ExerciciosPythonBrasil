#Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#   a - Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#   b - Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#   c- A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
# Faça um programa que determine o salário atual desse funcionário. 
# Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

salario = float(input('Salario: '))
ajuste = 1.5
anoInicial = int(input('Ano Inicio: '))
anoAtual = int(input('Ano Fim: '))
salario2 = salario

for i in range((anoInicial + 1), anoAtual + 1):
    ajuste = ajuste * 1
    atualSalario = salario2 + ((salario2 / 100) * ajuste)
    salario2 = atualSalario
    print('Salario inicial em {} foi de R$ {}! Em {}, o salário foi de R$ {}'.format(anoInicial,salario,i,atualSalario))
