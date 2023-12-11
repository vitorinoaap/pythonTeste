# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Qual o salário? '))

if sal <= 1250:
    novosal = sal + (sal * 15 / 100)
    percentual = 15
else:
    novosal = sal + (sal * 10 / 100)
    percentual = 10

print('Com o aumento de {}% o novo salário vai R$ {:.2f}'.format(percentual, novosal))
