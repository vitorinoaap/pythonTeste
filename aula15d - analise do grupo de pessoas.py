continua = ' '
anos18 = menos20 = homens = 0
while continua != 'N':
    idade = int(input('Qual a idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo? [M/F] ')).upper()

    if idade > 18:
        anos18 +=1
    if sexo == 'M':
        homens += 1
    elif idade < 20:
        menos20 += 1

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Mais informações? [S/N] ')).upper()

    print(25 * '-')

print(f'{anos18} pessoas tem mais de 18 anos')
print(f'{homens} homens foram cadastrados')
print(f'{menos20} mulheres tem menos de 20 anos')
print('FIM')
