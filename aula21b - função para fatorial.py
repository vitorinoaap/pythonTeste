def fatorial(num, show=False):
    """
    Calcula o fatorial de um número.
    :param num: número a ser calculado
    :param show: opcional para mostrar a conta
    :return: o fatorial do número informado
    """

    if show:
        print(f' {num} x', end='')
    cont = num - 1
    while cont > 0:
        num = num * cont
        if show:
            if cont > 1:
                print(f' {cont} x', end='')
            else:
                print(f' {cont} = ', end='')
        cont -= 1

    return num

print(25 * '-')
print(fatorial(5, True))
help(fatorial)
