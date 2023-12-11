nota1 = float(input('Primeira nota '))
nota2 = float(input('Segunda nota '))
media = (nota1 + nota2) / 2

print('A média é {:.1f}'.format(media))

if media < 5:
    print('REPROVADO')
# elif media >= 5 and media < 7:
elif 7 > media >= 5:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
