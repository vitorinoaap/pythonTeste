# pega o termo de razao em razao 10 vezes...

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
amais = 10
total = 0

while amais != 0:
    total = total + amais
    while cont <= amais:
        print('{}'.format(termo), end=' ')
        termo += razao
        cont += 1

    print('PAUSA')
    amais = int(input('Quantos termos vc quer a mais? '))
    cont = 1

print('Progressão finalizada com {} termos mostrados.'.format(total))
