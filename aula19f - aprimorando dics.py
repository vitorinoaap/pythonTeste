jogador = dict()
gols = list()
time = list()

while True:
    jogador.clear()
    gols = list()
    jogador['nome'] = str(input('Qual o nome do jogador? '))
    jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for i in range(1, jogos+1):
        gols.append(int(input(f'Quantos gols na partida {i}? ')))

    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    continua = str(input('Quer continuar: [S/N]')).upper()
    if continua == 'N':
        break

print('-=' * 30)
print(time)
print('-=' * 30)

print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    dados = int(input('Mostrar dados de qual jogador: [999 para parar]'))
    if dados == 999:
        break
    else:
        if dados > len(time) - 1:
            print('JOGADOR NÃO EXISTE')
        else:
            print(f'--- Levantamento do jogador {time[dados]["nome"]}')
            print(f'O jogador {time[dados]["nome"]} jogou {len(time[dados]["gols"])} partidas.')
            for i, v in enumerate(time[dados]['gols']):
                print(f'  => Na partida {i+1}, fez {v} gols.')
print('======= FIM ========')
