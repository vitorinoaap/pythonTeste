temp = list()
relacao = list()
mais = menos = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(relacao) == 0:
        mais = menos = temp[1]
    else:
        if temp[1] > mais:
            mais = temp[1]
        if temp[1] < menos:
            menos = temp[1]

    relacao.append(temp[:])
    temp.clear()

    continua = str(input('Quer continuar? [s/n] ')).upper()
    if continua == 'N':
        break

print(f'Ao todo você cadastrou {len(relacao)} pessoas.')
print(f'O maior peso foi de {mais}.  Peso de', end=' ')
for p in relacao:
    if p[1] == mais:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menos}.  Peso de', end=' ')
for p in relacao:
    if p[1] == menos:
        print(f'[{p[0]}]', end=' ')
print()
