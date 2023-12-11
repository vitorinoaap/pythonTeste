# Veja como utilizar o código \033[m com todas as suas principais possibilidades.
print('\033[4;31;43mOlá mundo!\033[m')
print('ok')

a = 3
b = 5
print('Os valors são \033[32m{} e \033[31m{}\033[m'.format(a, b))
print('ok')

nome = 'Vitorino'
print('olá, {}{}{}!!!!!!!!'.format('\033[4;34m', nome, '\033[m'))
print('ok')

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('olá, {}{}{}!!!!!!!!'.format(cores['amarelo'], nome, cores['limpa']))
print('ok')

