# divisão de valores em várias listas

valores = list()
pares = list()
impares = list()

while True:
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja continuar? [S/N] '))
    if resposta in 'Nn':
        break

for indice, valor in enumerate(valores):
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)
print('¨'*50)
print(f'Voce digitou os valores {valores}')
print(f'A lista com números pares é {pares}')
print(f'A lista com números ímpares é {impares}')

