def leiadinheiro(msg):
    # ler = True
    # n = ''
    # while ler:
    #     n = input(msg).replace(',', '.').strip()
    #
    #     if n.isalpha() or n == '':
    #         print(f'{n} é um valor inválido!')
    #     else:
    #         ler = False
    #
    ler = True
    while ler:
        try:
            n = input(msg).replace(',', '.').strip()
        except KeyboardInterrupt:
            print('  O usuário preferiu não informar os dados')
            nn = 0
            break

        try:
            nn = float(n)
        except (ValueError, TypeError):
            print('Tivemos um problema com os tipos de dados que vc digitou.')
        else:
            ler = False

    return nn
