dist = float(input('Qual a distancia em km da viagem? '))

'''if dist <= 200:
    valor = dist * 0.50
else:
    valor = dist * 0.45'''

valor = dist * 0.50 if dist <= 200 else dist * 0.45

print('O valor da passagem será de R$ {:.2f}'.format(valor))
