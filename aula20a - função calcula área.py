def area(a, b):
    print(f'A área de um terreno {larg} x {comp} é de {a*b} m2')


print('     CONTROLE DE TERRENOS')
print('=' * 30)
larg = float(input('Largura (m) '))
comp = float(input('Comprimento (m) '))
area(larg, comp)
