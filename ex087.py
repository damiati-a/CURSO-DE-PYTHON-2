# matriz 2.0
# somas de colunas e linhas
# maior valor da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maior = somacol = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = float(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('<>'*20)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]

    print()
print('<>'*20)
print(f'A soma dos valores pares da matriz é {somapar}')

for linha in range(0, 3):
    somacol += matriz[linha][2]
print(f'A soma dos elementos da terceira coluna é de {somacol}')

for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da segunda coluna é {maior}')


