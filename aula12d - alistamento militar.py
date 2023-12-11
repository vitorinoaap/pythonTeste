from datetime import date

anoatual = date.today().year  # pega o ano atual do computador

anonasc = int(input('Ano do nascimento '))

anos = anoatual - anonasc

print('Quem nasceu em {} tem {} anos em {}.'.format(anonasc, anos, anoatual))

if anos == 18:
    print('Está na hora de se alistar!')
elif anos < 18:
    print('Ainda falta {} ano(s) para se alistar.'.format(18 - anos))
    print('Seu alistamento será em {}'.format(anoatual + (18 - anos)))
elif anos > 18:
    print('Já se passou {} ano(s) do prazo do alistamento.'.format(anos - 18))
    print('O alistamento seria em {}'.format(anoatual - (anos - 18)))
