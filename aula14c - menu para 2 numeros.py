from time import sleep
opc = 0
while opc != 5:
    opc = 0
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    while opc != 4 and opc != 5:
        print('''-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair''')
        opc = int(input('Qual a sua opção? '))
        if opc == 1:
            print('A soma entre {} e {} é {}.'.format(n1, n2, n1+n2))
        elif opc == 2:
            print('{} x {} = {}'.format(n1, n2, n1 * n2))
        elif opc == 3:
            print('O maior número é {}.'.format(n1 if n1 > n2 else n2))
        elif opc > 5:
            print('Opção inválida.')
        sleep(1)
