mesAno = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
tempMes = []

for i in range(0, len(mesAno)):
    temp = float(input("Temperatura media do mês de "+ mesAno[i] +": "))
    tempMes.append(temp)

mediaAnual = sum(tempMes) / len(tempMes)

for i in range(0, len(tempMes)):
    if tempMes[i] > mediaAnual:
        print(str(i+1) + " - "+ mesAno[i])