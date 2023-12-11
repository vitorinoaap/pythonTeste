pessoa = dict()
pessoas = list()
totidade = mediaidade = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    totidade += pessoa['idade']
    pessoas.append(pessoa.copy())
    continua = str(input('Quer continuar? [S/N]')).upper()
    if continua == 'N':
        break

print(pessoas)
print('-='*30)
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas.')
mediaidade = totidade / len(pessoas)
print(f'A média de idade é de {mediaidade:.2f} anos.')
print('As mulheres cadastradas foram ', end=' ')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end=' ')

print()
print('Lista das pessoas que estão acima da média:')
for p in pessoas:
    if p['idade'] >= mediaidade:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('===FIM===')