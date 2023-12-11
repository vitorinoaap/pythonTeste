sexo = ' '
while sexo not in 'FM':
    sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()[0]  #o [0] pega a 1a letra informada
    print('Sexo registrado com sucesso.' if sexo in 'FM' else 'Dados inválidos.')
