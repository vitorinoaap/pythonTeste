from random import randint
from time import sleep
def sortea():
    print('Sorteando 5 valores para a lista: ', end=' ')
    for i in range(1, 6):
        num = randint(1, 10)
        print(num, end=' ')
        numeros.append(num)
        sleep(0.3)
    print('PRONTO!')


def somapar():
    par = 0
    for i in numeros:
        if i % 2 == 0:
           par += i
    print(f'Somando os valores pares de {numeros}, temos {par}')


numeros = list()
sortea()
somapar()
