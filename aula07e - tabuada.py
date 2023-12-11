num = int(input('Qual o numero? '))

print()
print('TABUADA DO {:=^10}'.format(num))
print(21 * '=')

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(1, 11):
# for i in lista:
    print(num, 'x', i, '=', num * i)

print('fim do for')
print()

i = 1

while i <= 10:
    print('{:2} x {:2} = {:2}'.format(num, i, num * i))
    i += 1

print('Fim do while')
print()
