from random import randrange
from time import sleep

print('-=-'*15)
print('Vou pensar em um numero entre 0 e 5.')
print('-=-'*15)

n = randrange(6)

print('Pensando...')

sleep(1)

num = int(input('Em qual número eu pensei? '))

if n == num:
    print('Parabéns!  Foi mesmo o número {}'.format(n))
else:
    print('Não foi desta vez.  Eu pensei no número {}'.format(n))
