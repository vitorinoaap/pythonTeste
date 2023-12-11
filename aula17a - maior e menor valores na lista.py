valores = []
for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))

print(f'Voce digitou os valores {valores}')
maior = max(valores)
menor = min(valores)
print(f'O maior valor foi {maior} nas posições', end=' ')
for c, v in enumerate(valores):
    if v == maior:
        print(c, end='...')
print()
print(f'O menor valor foi {menor} nas posições', end=' ')
for c, v in enumerate(valores):
    if v == menor:
        print(c, end='...')
