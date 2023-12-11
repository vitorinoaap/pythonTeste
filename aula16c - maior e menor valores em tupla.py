from random import randint
numeros = (randint(0,11), randint(0,11), randint(0,11), randint(0,11), randint(0,11))

print('Os valores sorteados foram:')
print(numeros)

print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
