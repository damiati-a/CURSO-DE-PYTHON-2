# tuplas com times de futebol
# os primeiros 5 colocados
# os 4 últimos
# ordem alfabética
# onde esta o SP

times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras',
         'Santos', 'Atlhetico-PR', 'RB Bragantino', 'Ceará', 'Corinthians', 'Atlético-GO',
         'Bahia', 'Sport', 'Fortaleza', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')

print('=='*150)
print(f'Lista de times do Brasileirão: {times}')
print('=='*150)
print(f'Os cinco primeiros colocados da tabela são: {times[0:5]}')
print('=='*150)
print(f'Os times que estão rebaixados são: {times[-4:]}')
print('=='*150)
print(f'Os times em ordem alfabética ficam: {sorted(times)}')
print('=='*100)
print(f'O São Paulo FC terminou na {times.index("São Paulo")+1}ª posição')