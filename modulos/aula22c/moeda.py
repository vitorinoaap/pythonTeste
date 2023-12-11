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
