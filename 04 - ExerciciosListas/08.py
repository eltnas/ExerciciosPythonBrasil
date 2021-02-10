#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

iddPessoa = []
altPessoa = []

lista = 1

while lista <= 5:
    print("Pessoa numero {}.".format(lista))
    idade = int(input("Idade : "))
    altura = float(input("altura: "))
    iddPessoa.append(idade)
    altPessoa.append(altura)
    lista += 1

print("Ordem digitada!")
print("Idade: {}   | Altura: {}".format(iddPessoa,altPessoa))
print("\n")
print("Ordem inversa!")
print("Idade: {}   | Altura: {}".format(iddPessoa[::-1],altPessoa[::-1]))
