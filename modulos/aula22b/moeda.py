def metade(n=0):
    return n / 2


def dobro(n=0):
    return n * 2


def aumentar(n=0, perc=0):
    return n + (n * perc/100)


def diminuir(n=0, perc=0):
    return n - (n * perc/100)


def moeda(n=0, moeda='R$'):  # se não informar qual a moeda aparece R$
    return f'{moeda}{n:>.2f}'.replace('.', ',')
