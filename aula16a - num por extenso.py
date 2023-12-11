num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entre 0 e 20 '))
    if n not in range(0, 21):
        print('Tente novamente.', end=' ')
    else:
        break

print(f'Você digitou o número {num[n]}')
