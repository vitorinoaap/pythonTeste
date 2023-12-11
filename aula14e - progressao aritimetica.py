# pega o termo de razao em razao 10 vezes...

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1

while cont <= 10:
    print('{}'.format(termo), end=' ')
    termo += razao
    cont += 1
