n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))

maior = n3
if n1 > n2 and n1 > n3:
    maior = n1
else:
    if n2 > n3:
        maior = n2

menor = n3
if n1 < n2 and n1 < n3:
    menor = n1
else:
    if n2 < n3:
        menor = n2

print('O maior número é o {} e o menor é o {}'.format(maior, menor))
