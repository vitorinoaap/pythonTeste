def maior(* n):  # Desempacota vários valores
    print('-=' * 30)
    print('Analisando os valores passados...')
    cont = m = 0
    for valor in n:
        cont += 1
        print(f'{valor} ', end=' ')
        if valor > m:
            m = valor
    print()
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor foi {m}')


maior(2, 9, 4, 5, 7, 1)
maior(2, 7)
maior(6)
maior()
maior(1, 3)
