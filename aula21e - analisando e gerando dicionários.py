def notas(*n, sit=False):
    """
    Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    aluno = {}
    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    aluno['media'] = sum(n) / len(n)
    if sit:
        if aluno['media'] >= 7:
            aluno['situação'] = 'BOA'
        elif aluno['media'] >= 5:
            aluno['situação'] = 'RAZOÁVEL'
        else:
            aluno['situação'] = 'RUIM'

    return aluno


resp = notas(10, 5.5, 6, 1, 4, sit=True)
print(resp)
help(notas)
