"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores."""

from datetime import date

maioridade = 0
menoridade = 0
anoatual = date.today().year  # pega o ano atual do computador

for c in range(1, 8):
    ano = int(input('Digite o ano da {}a pessoa: '.format(c)))
    if anoatual - ano > 17:
        maioridade += 1
    else:
        menoridade += 1

print('{} pessoas são maiores de idade e {} são menores de idade.'.format(maioridade, menoridade))
'''

lista_ano = []
idade = []
anoatual = date.today().year  # pega o ano atual do computador
for c in range (1, 4):
    ano_nascimento = int(input('Informe o ano de nascimento da {}ª pessoa: '.format(c)))
    lista_ano.append(ano_nascimento)
    idade.append(anoatual - ano_nascimento)
# print(lista_ano)
# print(idade)
menos_21 = 0
maior_21 = 0

for a in idade:
    if a < 21:
        menos_21 = menos_21 + 1
    else:
        maior_21 = maior_21 + 1

print()
# print('Quantas pessoas serão consideradas? {}{}{}.'.format('\033[1;32m',n,'\033[m'))
print()
print('Os anos de nascimentos informados são: {}{}{}.'.format('\033[1;34m',lista_ano,'\033[m'))
print()
print('As idades das pessoas informadas são: {}{}{}.'.format('\033[1;34m',idade,'\033[m'))
print()
print('São {}{}{} pessoas menores de idade (< 21 anos).'.format('\033[1;33m',menos_21,'\033[m'))
print()
print('São {}{}{} pessoas maiores de idade (>= 21 anos).'.format('\033[1;35m',maior_21,'\033[m'))
print()
# Escrevendo na tela FIM sublinhado e em vermelho.
print('\033[1;4;31m','FIM!','\033[m')
'''