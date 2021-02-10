vetor = []
vogal = ['A','E','I','O','U']
contVogal = 0
contConsoante = 0

for i in range(10):
    palavra = str(input("Escreva: ").upper())
    vetor.append(palavra)
    if palavra in vogal:
        contVogal = contVogal + 1
    else:
        contConsoante = contConsoante + 1

print("São {} consoantes!".format(contConsoante)) 