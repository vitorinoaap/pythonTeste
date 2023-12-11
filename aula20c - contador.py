def contador(ini, fim, passo):
    """
    Faz uma contagem e mostra  na tela
    :param ini: inicio da contagem
    :param fim: fim da contagem
    :param passo: passo da contagem
    :return: sem retorno
    Funcao criada por fulano...
    """
    if passo == 0:
        passo = 1

    print('=' * 30)
    print(f'Contagem de {ini} a {fim} de {passo} em {passo}')
    if passo > 0:
        for n in range(ini, fim+1, passo):
            print(f'{n} ', end=' ')
        print('FIM')
    else:
        for n in range(ini, fim-1, passo):
            print(f'{n} ', end=' ')
        print('FIM')


contador(1, 10, 1)
contador(10, 0, -2)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passos: '))
contador(i, f, p)
help(contador)
