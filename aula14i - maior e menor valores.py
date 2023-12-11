cont = num = total = maior = menor = media = 0
sn = 'S'
while sn == 'S':
    num = int(input('Digite um número: '))
    sn = ' '
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N] ')).strip().upper()[0]  #o [0] pega a 1a letra informada
    cont += 1
    total += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

media = total / cont
print(f'Você digitou {cont} números e a média foi de {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
