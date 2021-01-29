horasTrab = float(input("Quantas horas trabalhou esse mes? "))
valorHoras = float(input("Valor das horas: R$ "))

salBruto = horasTrab * valorHoras

if salBruto >= 2501:
	desc = 20
elif salBruto <= 2500 and salBruto >= 1501:
	desc = 10
elif salBruto <= 1500 and salBruto >= 901:
	desc = 5
else:
	desc = 0

salIR = (salBruto / 100) * desc
salINSS = (salBruto / 100) * 10
salFGTS = (salBruto / 100) * 11
totalDesc = salIR + salFGTS + salINSS
salLiquido = salBruto - totalDesc

print("Salário Bruto: (",valorHoras," * ", horasTrab,")        : R$  ", salBruto)
print("(-) IR (", desc ,"%)                           : R$  ",salIR)  
print("(-) INSS ( 10%)                          : R$  ", salINSS)
print("FGTS (11%)                               : R$  ", salFGTS)
print("Total de descontos                       : R$  ", totalDesc)
print("Salário Liquido                          : R$  ", salLiquido)