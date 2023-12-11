"""Programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""

nome = [1,2,3,4,5]
idade = [1,2,3,4,5]
sexo = [1,2,3,4,5]

# media = 0
# maisvelho = 0
# nomemaisvelho = 0
# menosdevinte = 0
media = maisvelho = nomemaisvelho = menosdevinte = 0

for c in range(1,5):
    print('{}a pessoa'.format(c))
    nome[c] = str(input('Nome: '))
    idade[c] = int(input('Idade: '))
    sexo[c] = str(input('Sexo: '))
    media += idade[c]
    if idade[c] > maisvelho and sexo[c] in 'mM':
        maisvelho = idade[c]
        nomemaisvelho = c
    if sexo[c] in 'fF' and idade[c] < 20:
        menosdevinte += 1

print('A média de idade do grupo é de {} anos.'.format(media/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(maisvelho, nome[nomemaisvelho]))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(menosdevinte))
