'''
a = int(input('Digite um número '))
b = int(input('Digite outro número '))
c = int(input('Digite mais um número '))
d = int(input('Digite o último número '))
valores = (a, b, c, d)
'''
# OU...

valores = (int(input('Digite um número ')),
           int(input('Digite outro número ')),
           int(input('Digite mais um número ')),
           int(input('Digite o último número ')))
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}a posição')
else:
    print('O valor 3 não apareceu em nenhuma posição')
print(f'Os valores pares digitados foram ', end=' ')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
