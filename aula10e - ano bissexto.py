from datetime import date

ano = int(input('Informe o ano (coloque 0 para o ano atual): '))

if ano == 0:
    ano = date.today().year  # pega o ano atual do computador

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('Esse ano {} não é bissexto'.format(ano))
