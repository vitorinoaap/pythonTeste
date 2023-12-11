def ficha(nome, gol):
    if nome == '':
        nome = '<desconhecido>'
    if gol == ''or not gol.isnumeric():
        gol = 0

    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')


jogador = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
ficha(jogador, gols)
