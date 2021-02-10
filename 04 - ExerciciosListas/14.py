pergunta = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]
resposta = ["Inocente","Inocente","Suspeita","Cúmplice","Cúmplice","Assassino"]
culpa = 0
x = 0

while x < len(pergunta):
    print(pergunta[x] + " (s/n)")
    resp = str(input("Resp.: ").upper())
    resposta.append(resp)
    if resp == 'S':
        x = x + 1
    elif resp == 'N':
        x = x + 1
    else:
        x = x
for i in range(len(resposta)):
    if resposta[i] == 'S':
        culpa += 1

print("O suspeito é "+ resposta[culpa])
