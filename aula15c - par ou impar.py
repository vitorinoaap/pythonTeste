from random import randint
cont = 0
ganhou = True
while ganhou:

    valor = int(input('Diga um valor '))
    pi = str(input('Par ou impar [P/I] ')).upper()
    print(25 * '=')
    computador = randint(0, 11)
    resultado = computador + valor

    if resultado % 2 == 0:  # resto da divisao por 2. Se = 0 é numero par.
        parimpar = 'PAR'
    else:
        parimpar = 'IMPAR'

    print(f'Você jogou {valor} e o computador {computador}. Total de {resultado}. DEU {parimpar}')

    if pi in parimpar[0]:
        cont += 1
        print('Você ganhou')
    else:
        ganhou = False
        print('Você perdeu')
        print(f'GAME OVER!  Você ganhou {cont} vezes')

    print(25 * '=')
