from random import randint
from operator import itemgetter
jogadores = dict()  # solução vi no youtube!
for c in range(1, 5):
    jogadores[f"jogador {c}"] = randint(1, 6)
# jogadores = {'jogador1': randint(1, 6), solução apresentada assim!
#              'jogador2': randint(1, 6),
#              'jogador3': randint(1, 6),
#              'jogador4': randint(1, 6)}
# jogadores['jogador1'] = randint(1, 6)  eu havia feito assim!
# jogadores['jogador2'] = randint(1, 6)
# jogadores['jogador3'] = randint(1, 6)
# jogadores['jogador4'] = randint(1, 6)
print(jogadores)

print('Valores sorteados:')
for jogador, num in jogadores.items():
    print(f'{jogador} tirou {num} no dado.')

# ranking = list()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(ranking)
print('-*' * 30)
print('  == Ranking dos jogadores ==')
for i, v in enumerate(ranking):
    print(f'  {i+1}o lugar: {v[0]} com {v[1]}.')

'''ATUALIZAÇÀO PYTHON 3.6+

Para quem chegou aqui, meus parabéns. Após uma pesquisada vi que a partir da versão 3.6 fizeram uma atualização 
(implementada oficialmente no 3.7) na questão de importar o itemgetter. O jeito do Guanabara não é mais o recomendado.

O que você vai colocar de argumento no sorted é o seguinte:
sorted(nome_do_dicionario.items(), key=lambda item: item[1], reverse=True))

O `key=lambda item: item[1]' faz com o sort seja feito a partir dos valores que os jogadores obtiveram. Se quiser fazer
com as chaves ao invés dos valores, use item[0]. Assim não precisar importar e fazer uso do itemgetter.

Abaixo vou adicionar meu código, que de certa forma ficou bem próximo do jeito que ele propôs também. Apenas 
automatizei com for o primeiro dicionário e transformei a lista do sorted em dicionário:

from random import randint
from time import sleep

jogos1 = {}
c = 1

for cont in range(1, 5):
    jogada = randint(1, 6)
    jogos1["jogador" + str(cont)] = jogada
print('Valores sorteados:')
for k, v in jogos1.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
print('-=' * 30)
print(f'{"== RANKING DOS JOGADORES ==":^30}')
jogos2 = dict(sorted(jogos1.items(), key=lambda item: item[1], reverse=True))
for k, v in jogos2.items():
    print(f'{c}o. lugar: {k} com {v}.')
    c +=1
    sleep(1)'''