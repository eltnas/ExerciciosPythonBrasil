print("Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:")
print("salário bruto. Quanto pagou ao INSS. Quanto pagou ao sindicato. O salário líquido.")
print("calcule os descontos e o salário líquido, conforme a tabela abaixo:")
print("+ Salário Bruto : R$")
print("- IR (11%) : R$")
print("- INSS (8%) : R$")
print("- Sindicato ( 5%) : R$")
print("= Salário Liquido : R$")

print("Dev: Elton C. Nascimento")
print("----------------------------------------------------")

porHora = float(input("Valor recebido por hora: "))
qtdHora = float(input("Horas mensais: "))

salBruto = (qtdHora * porHora)
salIR = (salBruto / 100) * 11
salINSS = (salBruto / 100) * 8
salSindicato = (salBruto / 100) * 5
salLiquido = salBruto - salIR - salINSS - salSindicato

print("+ Salário Bruto  : R$ ", salBruto)
print("- IR (11%)       : R$ ", salIR)
print("- INSS (8%)      : R$ ", salINSS)
print("- Sindicato (5%) : R$ ", salSindicato)
print("= Salário Liquido: R$ ", salLiquido)