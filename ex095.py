# Aprimorando dicionários, utilizando o codigo do 093

jogador = dict()
partidas = list()
time = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()

    for c in range(0, total):
        partidas.append(int(input(f'Quantos gols na partida {c + 1}: ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resposta = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas com S ou N.')
    if resposta == 'N':
        break

print('-' * 50)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-' * 50)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 50)

while True:
    busca = int(input('Mostrar os dados de qual jogador? [999 para cancelar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! NÃO CONTÉM JOGADOR COM O CÓDIGO INFORMADO {busca}!')
    else:
        print(f' -> LEVANTAMENTO DOS DADOS DO JOGADOR {time[busca["nome"]]}: ')
        for i, g in enumerate(time[busca]["gols"]):
            print(f' -> No jogo {i+1} fez {g} gols')
    print('-'*50)
print('O PIOR TIME É O SEU! VOLTE SEMPRE PARA MAIS BUSCAS.')

