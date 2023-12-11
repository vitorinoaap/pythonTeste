aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['status'] = 'Aprovado'
elif aluno['media'] < 5:
    aluno['status'] = 'Reprovado'
else:
    aluno['status'] = 'Recuperação'

print(aluno)
print(30 * '-=')
print(f'Nome é igual a {"nome"}')
print(f'Média é igual a {aluno["media"]}')
print(f'Situação é igual a {aluno["status"]}')
print(30 * '-=')
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
