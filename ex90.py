# boletim com dicionarios

aluno = dict()

aluno['nome'] = str(input('Nome do Aluno: '))
aluno['media'] = float(input(f'Nota do(a) {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for chave, valor in aluno.items():
    print(f'* {chave} = {valor}')


