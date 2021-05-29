# um programa que mostre as pessoas mais pesadas
# quantas pessoas foram cadastradas
# mostrar as pessoas mais leves

pessoas = list()
principal = list()
maior = menor = 0

while True:
    pessoas.append(str(input(f'Nome da pessoa: ')))
    pessoas.append(float(input(f'Peso da pessoa: ')))
    if len(principal) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        elif pessoas[1] < menor:
            menor = pessoas[1]
    principal.append(pessoas[:])
    pessoas.clear()
    resposta = str(input('Dejesa prosseguir? [S/N] '))
    if resposta in 'Nn':
        break

print('<>'*40)
print(f'Os dados foram {principal}')
print(f'Ao todo, foram cadastradas {len(principal)} pessoas. Peso de ', end='')
print(f'O maior peso foi de {maior}KG')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {menor}KG. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
print()
