from datetime import date

anoatual = date.today().year  # pega o ano atual do computador

nasc = int(input('Qual o ano de nascimento do atleta? '))

anos = anoatual - nasc

if anos <= 9:
    categoria = 'MIRIM'
elif anos <= 14:
    categoria = 'INFANTIL'
elif anos <= 19:
    categoria = 'JÚNIOR'
elif anos <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print('O atleta tem {} anos e portanto ele é classificado como {}'.format(anos, categoria))
