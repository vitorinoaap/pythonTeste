from random import randint
from time import sleep
mega = []
jogos = []

print(40 * '-')
print('{:^40}'.format(' MEGASENA '))
print(40 * '-')

quant = int(input('Quantos jogos quer: '))

print(f'Sorteando {quant} jogos...')

''' # Minha solução não trabalha com lista composta
for i in range(1, quant + 1):
    for cont in range(1, 7):
        while True:
            num = randint(1, 60)
            if num not in mega:
                mega.append(num)
                break
    mega.sort()
    print(f'Jogo {i}: {mega}')
    mega.clear()
    sleep(.5)
print(40 * '-')
print('BOA SORTE!!!')
'''
# Solução com lista composta

for i in range(1, quant + 1):
    for cont in range(1, 7):
        while True:
            num = randint(1, 60)
            if num not in mega:
                mega.append(num)
                break
    mega.sort()
    jogos.append(mega[:])
    mega.clear()

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(.5)
print('=' * 5, '  BOA SORTE  ', '=' * 5)
