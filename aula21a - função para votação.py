'''def valida(a):
    from datetime import date
    ano = date.today().year  # pega o ano atual do computador
    anos = ano - a
    if anos < 16:
        votar = 'NÃO VOTA'
    elif anos > 65:
        votar = 'OPCIONAL'
    else:
        votar = 'OBRIGATORIO'
    print(f'Com {anos} anos voto {votar}')


ano = int(input('Em que ano voce nasceu? '))
valida(ano)
'''
# OU........

def valida(a):
    from datetime import date
    ano = date.today().year  # pega o ano atual do computador
    anos = ano - a
    if anos < 16:
        return f'Com {anos} anos: NÃO VOTA'
    elif anos > 65:
        return f'Com {anos} anos: VOTO OPCIONAL'
    else:
        return f'Com {anos} anos: VOTO OBRIGATORIO'


ano = int(input('Em que ano voce nasceu? '))
print(valida(ano))
