valores = []
continua = ' '
while continua != 'N':
    valor = int(input('Digite um valor: '))

    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado.  Não vou adicionar...')

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]')).upper().strip()

print(30*'-=')
valores.sort()
print(f'Você digitou os valores {valores}')
