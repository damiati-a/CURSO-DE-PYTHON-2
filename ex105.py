# analise de dados e gerando um dicionário de forma opicional


def notas(*n, situaçao=False):
    """
    -> FUNÇAO PARA ANÁLISE DE NOTAS E SITUAÇÃO DE ALUNOS
    :param n: UMA OU MAIS NOTAS DE UM ALUNO
    :param situaçao: VALOR OPICIONAL, INDICANDO O STATUS DA SITUAÇÃO DO ALUNO
    :return: DICIONÁRIO COM VÁRIAS INFORMAÇÕES SOBRE A SITUAÇÃO DO ALUNO
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)

    if situaçao:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resposta = notas(5, 1.9, 8, 5, situaçao=True)
print(resposta)
help(notas)
