from datetime import date
anoatual = date.today().year  # pega o ano atual do computador
trab = dict()

trab['nome'] = str(input('Nome: '))
ano = int(input('Ano do nascimento: '))
trab['idade'] = anoatual - ano
trab['carteira'] = int(input('Carteira de trabalho (0) não tem: '))
print(trab)
if trab['carteira'] > 0:
    trab['contratação'] = int(input('Ano de contratação: '))
    trab['salario'] = float(input('Salário: R$ '))
    trab['aposentadoria'] = trab['idade'] + ((trab['contratação'] + 35) - anoatual)
    print(trab)
print('=-' * 30)
for k, v in trab.items():
    print(f'{k} tem o valor {v}.')
