import math
## ou from math import sin, radians, cos, tan - e retirar as referencias a math.

angulo = float(input('Digite o angulo: '))

print('O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(math.sin(math.radians(angulo)), math.cos(math.radians(angulo)), math.tan(math.radians(angulo))))

# print(dir(math))
