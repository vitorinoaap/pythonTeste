valor = float(input('Qual valor você quer sacar? R$'))
print(25 * '=')

cont = 0
lista = [200, 100, 50, 20, 10, 1]
notas = len(lista)  # diversidade de cédulas, 6 aqui no caso.
for i in range(0, notas):
    while valor >= lista[i]:
        cont += 1
        valor -= lista[i]

    if cont > 0:
        print(f'Total de {cont} cédulas de R${lista[i]}')
        cont = 0

print('FIM')
