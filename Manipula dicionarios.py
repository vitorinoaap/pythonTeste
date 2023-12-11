pessoas = {'nome': 'vitorino', 'sexo': 'M', 'idade': 60}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}')
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')

estado1 = {'uf': 'rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'sao paulo', 'sigla': 'SP'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    print(e)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
