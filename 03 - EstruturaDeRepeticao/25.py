#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

qtdPessoas = int(input('Quantas pessoas: '))
count = 0
idade = []

while count < qtdPessoas:
    idade2 = idade.append(int(input('Idade: ')))
    count += 1

mediaIdade = sum(idade) / qtdPessoas
if mediaIdade <= 25:
    print('A media das idades é {}, o grupo é jovem!'.format(mediaIdade))
elif mediaIdade >= 26 and mediaIdade <= 60:
    print('A media das idades é {}, o grupo é Adulta!'.format(mediaIdade))
else:
    print('A media das idades é {}, o grupo é Idosa!'.format(mediaIdade))