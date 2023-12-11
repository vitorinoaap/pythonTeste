num = int(input('Qual o número? '))
opc = int(input('''Qual a base?
[1] para binário
[2] para octal
[3] para hexadecimal
'''))

if opc == 1:
    print('O número {} convertido para binário é {}'.format(num, bin(num)))
    print('O número {} convertido para binário é {}'.format(num, bin(num)[2:])) #FATIA O RESULTADO RETIRANDO O 0b INICIAL
elif opc == 2:
    print('O número {} convertido para octal é {}'.format(num, oct(num)))
elif opc == 3:
    print('O número {} convertido para hexa é {}'.format(num, hex(num)))
else:
    print('OPÇÃO INVÁLIDA')

