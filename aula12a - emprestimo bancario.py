valor = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário? '))
anos = int(input('Quantos anos para pagar? '))
valormensal = valor / (anos * 12)
sal30pcento = sal * 30 / 100

print('Mensais de {:.2f}'.format(valormensal))

print('30 por cento do salario = {:.2f}'.format(sal30pcento))

if valormensal <= sal30pcento:
    print('Você pode pagar')
else:
    print('Você NÃO pode pagar')
