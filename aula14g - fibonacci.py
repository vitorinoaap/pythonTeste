n = int(input('Quantos termos quer? '))
a = c = cont = 0
b = 1
while cont < n:
    print(f'{c}', end=' ')
    a = b
    b = c
    c = a + b
    cont += 1
print('FIM')

'''

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


fib(500)
'''