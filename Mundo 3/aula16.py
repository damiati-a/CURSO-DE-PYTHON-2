# DICIONARIOS

"""
IDENTIFICAÇÃO DAS ESTRUTURAS COMPOSTAS

TUPLAS ()
LISTA []
DICIONARIOS {} - dados = dict()

--------------------------------------------
dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome']) == Pedro

Para adicionar novos dados
dados['sexo'] = M
Assim automaticamente ele será criado e adicionado no dicionario

Para deletar
del dados['idade']

"""
"""
# pessoas = {'nome': 'André', 'sexo': 'M', 'idade': 23}
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

pessoas = {'nome': 'André', 'sexo': 'M', 'idade': 23}
print(pessoas.items())  # formam uma lista formada por tuplas
# del pessoas['sexo']
pessoas['nome'] = 'Reginaldao'
pessoas['peso'] = 77
for k, v in pessoas.items():  # k == keys(chaves)
    print(f'{k} = {v}')

"""
"""
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1])
"""
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())  # .copy é semelhante ao uso do fatiamento [:]
print(brasil)
