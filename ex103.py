# contador de gols de um jogador
# mesmo sem dados o programa entende e consegue retornar com uma resposta


def ficha(jogador='<desconhecido>', bola=0):
    print(f'O jogador {jogador} fez {bola} gol(s) no campeonato.')


nome = str(input("nome do Jogador: "))
gols = str(input("Número de gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(bola=gols)
else:
    ficha(nome, gols)

