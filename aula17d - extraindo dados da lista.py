lista = list()

while True:
    lista.append(int(input('Digite um valor: ')))
    continua = str(input('Quer continuar: [S/N]')).upper()
    if continua == 'N':
        break

print(f'Você digitou {len(lista)} elementos.')

lista.sort(reverse=True)

print(f'Os valores em ordem decrescente são {lista}')

if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
