par1 = par2 = 0
expressao = input(str('Digite a expressão: '))

for n in expressao:
    if n == '(':
        par1 += 1
    elif n == ')':
        par2 += 1

if par1 == par2:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está errada.')

# OU............................................

expr = input(str('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está errada.')
