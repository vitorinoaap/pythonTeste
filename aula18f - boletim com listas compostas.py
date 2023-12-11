relacao = list()
temp = list()

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    relacao.append(temp[:])
    temp.clear()
    continua = str(input('Quer continuar? [S/N]')).upper()
    if continua == 'N':
        break

print('=' * 40)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')  # No. alinhado a direita,
                                              # Nome alinhado a direita e Média alinhada a esquerda
for i in range(0, len(relacao)):
    print(f'{i:2}  {relacao[i][0]:<4}  {(relacao[i][1] + relacao[i][2]) / 2:>10}')

while True:
    print(40 * '-')
    aluno = int(input('Mostrar notas de qual aluno? [999 interrompe] '))
    if aluno == 999:
        break
    else:
        if aluno > len(relacao) - 1:
            print('Aluno não existe!')
        else:
            print(f'Notas de {relacao[aluno][0]} são {relacao[aluno][1]}, {relacao[aluno][2]}')
print('    Fim')
