matriz = [[], [], []]
for lin in range(0, 3):
    for col in range(0, 3):
        # matriz[lin][col] = int(input(f'Digite o valor para [{lin, col}]: '))
        num = int(input(f'Digite o valor para [{lin, col}]: '))
        matriz[lin].append(num)
print(40 * '-=')
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^5}]', end='')
    print()
