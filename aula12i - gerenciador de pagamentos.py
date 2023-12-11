""" Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros"""

print('{:=^40}'.format(' Lojas Vitorino '))

valor = float(input('Qual o valor do produto? R$ '))
newvalor = valor   # apenas para não dar erro se escolher opc inválida.

print('''
Escolha uma opção para pagamento

[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros''')
opc = int(input(': '))

if opc == 1:
    newvalor = valor - (valor * 10 / 100)
    print('Você terá R$ {:.2f} de desconto!'.format(valor * 10 / 100))
elif opc == 2:
    newvalor = valor - (valor * 5 / 100)
    print('Você terá R$ {:.2f} de desconto'.format(valor * 5 / 100))
elif opc == 3:
    newvalor = valor
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra será realizada em {}X de R$ {:.2f} sem juros'.format(parcelas, newvalor / parcelas))
elif opc == 4:
    newvalor = valor + (valor * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra será realizada em {}X de R$ {:.2f} com juros'.format(parcelas, newvalor / parcelas))
else:
    print('Opc inválida!')

print('O valor final a ser pago será de R$ {:.2f}'.format(newvalor))
