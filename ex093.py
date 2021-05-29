# cadastro de jogador, quantidade de gols por partida e total
# gerenciamento de carreira

jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0, total):
    partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-'*50)
print(jogador)
print('-'*50)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-'*50)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for i, v in enumerate(jogador["gols"]):
    print(f' -> Na partida {i+1}, fez {v} gols')

