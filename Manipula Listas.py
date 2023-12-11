'''
lanche = ['hamburguer','suco','pizza','sorvete']
for i in lanche:
    print(i)
lanche.append('cookie')  # adiciona elemento ao fim da lista
print(lanche)
lanche.insert(0, 'cachorro quente')  # adiciona elemento em determinada posição
print(lanche)
del lanche[3]  # apaga determinado elemento
print(lanche)
lanche.pop(2)
print(lanche)
lanche.remove('cachorro quente')
if 'cachorro quente' in lanche:  # testa se o elemento existe pra não dar erro
    lanche.remove('cachorro quente')
print(lanche)
lanche.pop()  # se não informa o indice, elimina o último elemento
print(lanche)

valores = list(range(4, 11))  # cria LISTA
print(valores)

valores = [8, 3, 5, 4, 9, 3, 0]
print(valores)
valores.sort()  # coloca em ordem
print(valores)
valores.sort(reverse=True)  # coloca em ordem decrescente
print(valores)
print(len(valores))  # print o tamanho da lista

valores = []  # inicia uma lista vazia
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...', end='')
print()
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...')

# dá entrada na lista pelo teclado
valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...')

a = [2, 3, 4, 7]
b = a
print(a)
print(b)
b[2] = 8  # o python cria uma ligação entre as listas.  mexeu em uma altera a outra...
print(a)
print(b)
b = a[:]  # agora criou uma cópia, não existe mais a ligação...
b[1] = 9
print(a)
print(b)
'''
# AULA 18--LISTAS COMPOSTAS-----------------

teste = list()
teste.append('vitorino')
teste.append(60)
print(teste)
galera = list()
galera.append(teste)
teste[0] = 'maria'
teste[1] = 22
galera.append(teste)
print(galera)

teste = list()
teste.append('vitorino')
teste.append(60)
print(teste)
galera = list()
galera.append(teste[:])
teste[0] = 'maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['joão', 19], ['ana', 22], ['joaquim', 13], ['maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
for p in galera:
    print(p)
for p in galera:
    print(p[0])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])  # Cria uma cópia, não um link.
    dado.clear()
print(galera)
totmai = totmen = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
