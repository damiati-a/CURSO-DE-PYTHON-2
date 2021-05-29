# maior e menos da lista

valor = list()
maior = 0
menor = 0

for n in range(0, 5):
    valor.append(int(input(f'Digite um valor para a posição {n}: ')))
    if n == 0:
        maior = menor = valor[n]
    else:
        if valor[n] > maior:
            maior = valor[n]
        if valor[n] < menor:
            menor = valor[n]


print('='*20)
print(f'Você digitou os valores {valor}')
print(f'O maior valor digitado foi {maior}, nas posições ', end='')
for i, v in enumerate(valor):
    if v == maior:
        print(f'{i}, ', end='')
print(f'\nO menor valor digitado foi {menor}, nas posições ', end='')
for i, v in enumerate(valor):
    if v == menor:
        print(f'{i}, ', end='')

