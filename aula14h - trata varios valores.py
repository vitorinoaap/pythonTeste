#
parar = soma = cont = 0

while parar != 999:
    parar = int(input('Digite um número [999] para parar: '))
    if parar != 999:
        soma += parar
        cont += 1

print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
