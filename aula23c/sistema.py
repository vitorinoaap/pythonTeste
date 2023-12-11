"""
Criando um menu
"""
# from aula23c.lib.interface import *
from aula23c.lib.arquivo import *
# from os import system     #para apagar a tela no pycharm
                            #deve ir em run > modify run config > emulate terminal....

arq = 'cursoemvideo.txt'
opções = ['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema']

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    criarArquivo(arq)

while True:
    # system('cls')
    resposta = menu(opções)
    if resposta == 1:
        # cabecalho(opções[0])
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho(opções[1])
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Finalizando...')
        break
    else:
        print('\033[31mERRO: Opção inválida\033[m')
