#importa somente o metodo hypot
from math import hypot

lado1 = float(input('Lado 1: '))
lado2 = float(input('Lado 2: '))
print('A hipotenusa é {:.2f}'.format(hypot(lado1, lado2)))
