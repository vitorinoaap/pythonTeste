r1 = float(input('Reta 1 '))
r2 = float(input('Reta 2 '))
r3 = float(input('Reta 3 '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar triângulo. ', end='')   # CONTINUA A IMPRIMIR NA MESMA LINHA
    if r1 == r2 == r3:
        print('É um triângulo EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('É um triângulo ESCALENO')
    else:
        print('É um triângulo ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo')
