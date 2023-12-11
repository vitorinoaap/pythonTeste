totgasto = tot1000 = menorvalor = 0

while True:
    produto = str(input('Nome do produto '))
    valor = float(input('Valor R$'))

    totgasto += valor

    if valor > 1000:
        tot1000 += 1

    if menorvalor == 0 or valor < menorvalor:
        menorvalor = valor
        maisbarato = produto

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Mais informações? [S/N] ')).upper().strip()[0]

    print(25 * '-')

    if continua == 'N':
        break

print(f'O total da compra foi R${totgasto:.2f}')
print(f'Temos {tot1000} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {maisbarato} que custa R${menorvalor:.2f}')
print('{:-^40}'.format(' FIM DO PROGRAMA '))