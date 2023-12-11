n = int(input('Informe o número '))

resultado = n % 2  #resto da divisao por 2. Se = 0 é numero par.

if resultado == 0:
    print('Esse número é PAR')
else:
    print('Esse número é impar')

print('Esse número é PAR' if resultado == 0 else 'Esse número é IMPAR')
