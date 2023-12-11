valor = float(input('Qual valor você quer sacar? R$'))
cont50 = cont20 = cont10 = cont1 = 0

while valor >= 50:
    cont50 += 1
    valor -= 50

while valor >= 20:
    cont20 += 1
    valor -= 20

while valor >= 10:
    cont10 += 1
    valor -= 10

while valor >= 1:
    cont1 += 1
    valor -= 1

print(25 * '=')
if cont50 > 0:
    print(f'Total de {cont50} cédulas de R$50,00')
if cont20 > 0:
    print(f'Total de {cont20} cédulas de R$20,00')
if cont10 > 0:
    print(f'Total de {cont10} cédulas de R$10,00')
if cont1 > 0:
    print(f'Total de {cont1} cédulas de R$1,00')
print(25 * '=')

# OU.......

valor = float(input('Qual valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('FIM')
