from random import randrange

print('-=-'*15)
print('Vou pensar em um numero entre 0 e 10.')
print('-=-'*15)

n = randrange(11)

vezes = 0
num = 11
while n != num:
    num = int(input('Em qual número eu pensei? '))
    vezes += 1
    if n != num:
        if n > num:
            print('Mais... Tente novamente')
        else:
            print('Menos... Tente novamente.')

print('Parabéns!  Foi mesmo o número {}.  Acertou com {} tentativas.'.format(n, vezes))
