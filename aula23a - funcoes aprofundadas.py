def leiaint(msg):

    while True:
        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print('Erro: Digite um número inteiro válido.')

        except KeyboardInterrupt:
            print('  O usuário preferiu não informar os dados')
            n = 0
            break
        else:
            break
    return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))

        except (ValueError, TypeError):
            print('Erro: Digite um número real válido.')

        except KeyboardInterrupt:
            print('  O usuário preferiu não informar os dados')
            n = 0
            break
        else:
            break
    return n


num = leiaint('Digite um número inteiro: ')
print(f'O valor digitado foi {num}')
real = leiafloat('Digite um número real: ')
print(f'O valor digitado foi {real}')
