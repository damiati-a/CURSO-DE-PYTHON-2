# unindo dicionarios e listas
# quantas pessoas cadastradas
# media de idade
# lista de mulheres
# lista com os de idade acima da media

galera = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F/OUTRO] ')).upper()[0]
        if pessoa['sexo'] in 'M F OUTRO':
            break
        print('ERRO! Por gentileza, digite apenas M, F ou Outro.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resposta = str(input('Deseja continuar? [S/N] ')).upper()
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas com S ou N.')
    if resposta == 'N':
        break

print('-'*40)
print(f' -> Ao todo temos {len(galera)} pessoas cadastradas. ')
media = soma / len(galera)
print(f' -> A média de idade é de {media:5.2f} anos.')
print(' -> As mulheres cadastradas foram: ', end='')

for mulher in galera:
    if mulher['sexo'] in 'fF':
        print(f'{mulher["nome"]}; ', end='')
print()
print(' -> Lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('\nFIM DO CADASTRO, OBRIGADO POR PARTICIPAR!')

