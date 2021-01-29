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