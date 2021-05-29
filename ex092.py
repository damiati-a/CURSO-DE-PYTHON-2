# cadastro de trabalhador
# lendo nome, ano de nascimento
# ano de contratação e quando se aposenta

from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))

nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

print('=='*30)
for chave, valor in dados.items():
    print(f'* {chave} tem o valor de {valor}')
