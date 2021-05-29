# Listas parte 2

"""
append = adiciona elementos numa lista

dados = list()
dados.append('ze')
dados.append(20)
print(dados[0]) = 'ze'
print(dados[1] = '20'
"""
"""
pessoas = list()
pessoas.append(dados[:])  # gerando um fatiamento ou uma cópia de dados
# assim se pode ter uma lista dentro de outra lista

pessoas = [['gato',20], ['dog',12], ['galinha', 34]]   == tendo indice 0, 1 e 2
print(pessoas[0][0])  == ele printa o primeiro indice ['gato', 20] e o primeiro item deste indice ['gato]
"""
"""
teste = list()
teste.append('André')
teste.append(23)

galera = list()
galera.append(teste[:])

teste[0] = 'zezão'
teste[1] = 100
galera.append(teste[:])
print(galera)

"""
"""
galera = [['zé', 23]], ['feioso', 34], ['eu gostoso', 90]
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos')
"""
galera = list()
dado = list()
totmaior = totmenor = 0

for c in range(0,3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])  # caso não coloque o [:] ao dar .clear() a lista irá aparecer vazia
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1

print(f'temos {totmaior} maiores e {totmenor} menores de idade')
