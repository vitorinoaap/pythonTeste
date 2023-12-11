valores = list()
par = list()
impar = list()

while True:
    valores.append(int(input('Digite um valor: ')))
    continua = str(input('Quer continuar: [S/N]')).upper()
    if continua == 'N':
        break

print(30 * '=')
print(f'A lista completa é {valores}')

for n in valores:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

par.sort()
impar.sort()
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
