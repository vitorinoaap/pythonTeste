matriz = [[], [], []]
pares = maior = coluna3 = 0
for lin in range(0, 3):
    for col in range(0, 3):
        num = int(input(f'Digite o valor para [{lin, col}]: '))
        matriz[lin].append(num)
print(40 * '-=')
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^5}]', end='')
        if matriz[lin][col] % 2 == 0:
            pares += matriz[lin][col]
        if col == 2:
            coluna3 += matriz[lin][col]
        if lin == 1:
            if matriz[lin][col] > maior:
                maior = matriz[lin][col]
    print()
print(40 * '-=')
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {coluna3}')
print(f'O maior valor da segunda linha é {maior}')
