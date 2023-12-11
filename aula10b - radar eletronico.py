vel = float(input('Qual a velocidade do carro? '))

if vel <= 80:
    print('Tudo ok')
else:
    print('Você ultrapassou o limite de 80km/h e portanto deverá pagar R$ {:.2f}'.format((vel-80)*7))


