from random import randint
from time import sleep
lista = ('Pedra', 'Papel', 'Tesoura')
print('''
Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
opc = int(input('Escolha uma '))
computador = randint(0, 2)
print('Computador jogou {}'.format(lista[computador]))
sleep(2)
if computador == 0:
    if opc == 0:
        print('EMPATE')
    elif opc == 1:
        print('Jogador vence')
    elif opc == 2:
        print('Computador Vence')
    else:
        print('Jogada inválida')
elif computador == 1:
    if opc == 0:
        print('Computador vence')
    elif opc == 1:
        print('Empate')
    elif opc == 2:
        print('Jogador Vence')
    else:
        print('Jogada inválida')
elif computador == 2:
    if opc == 0:
        print('Jogador vence')
    elif opc == 1:
        print('Computador vence')
    elif opc == 2:
        print('Empate')
    else:
        print('Jogada inválida')

# não sei se as regras desse jogo idiota estão certas...
