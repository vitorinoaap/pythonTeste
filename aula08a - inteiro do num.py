import math

num = float(input('Digite o valor: '))

print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.floor(num)))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))

