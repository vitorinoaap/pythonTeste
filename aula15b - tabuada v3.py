# Digitando numero negativo encerra.
while True:
    print(25 * '=')
    num = int(input('Tabuada de qual o numero? '))
    print(25 * '=')

    if num < 0:
        break

    print()
    print(f'TABUADA DO {num:=^10}')
    print(21 * '=')

    for i in range (1, 11):
        print(f'{num:2} x {i:2} = {num*i:2}')

print('Tabuada encerrada!')
