def metade(n=0, formata=False):
    res = n / 2
    return res if not formata else moeda(res)


def dobro(n=0, formata=False):
    res = n * 2
    return res if not formata else moeda(res)


def aumentar(n=0, perc=0, formata=False):
    res = n + (n * perc/100)
    return res if not formata else moeda(res)


def diminuir(n=0, perc=0, formata=False):
    res = n - (n * perc/100)
    return res if not formata else moeda(res)


def moeda(n=0, moeda='R$'):  # se não informar qual a moeda aparece R$
    return f'{moeda}{n:>.2f}'.replace('.', ',')


def resumo(valor=0, mais=0, menos=0, formata=False):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'Preço analisado: \t{moeda(valor, "uuxxuS")}')   # \t tabulação
    print(f'Dobro do preço: \t{dobro(valor, formata)}')
    print(f'Metade do preço: \t{metade(valor, formata)}')
    print(f'{mais}% de aumento: \t{aumentar(valor, mais, formata)}')
    print(f'{menos}% de redução: \t{diminuir(valor, menos, formata)}')
    print('-' * 40)
