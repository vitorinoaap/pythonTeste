def contador(* n):  # Desempacota vários valores
    for valor in n:
        print(f'{valor} ', end=' ')
    print('FIM')


def dobra(lst):  # Trabalha com uma lista
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


def somar(a=0, b=0, c=0):
    """
    Funcao com parametros opcionais.  Pode deixar de
    passar que não vai dar erro.
    :param a:
    :param b:
    :param c:
    :return:
    """
    s = a + b + c
    return s


def teste(b):
    global a  # Com o 'global' a variavel 'a' passou a ser global e portando sofre mudanças dentro da função...
    print(f'A variavel A vale {a}')
    a = 8


contador(2, 4, 6)
contador(2, 5, 7, 8, 9)
contador(1)

valores = [6, 3, 8, 2, 5]
dobra(valores)
print(valores)

r1 = somar(3, 2, 5)
r2 = somar(1, 8)
r3 = somar(b=4, c=9)
print(f'Os resultados foram {r1} {r2} {r3}')
print()

a = 5
teste(a)
print(f'A variavel A vale {a}')
