peso = float(input('Peso? '))
altura = float(input('Altura? '))
imc = peso / (altura ** 2)

print('O índice de massa corporal é {:.1f}'.format(imc))
