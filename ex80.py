# lista ordenada em repetições sem usar o .sort()

lista = []
for valor in range(0, 5):
    n = int(input('Digite um valor: '))
    if valor == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1

print('='*80)
print(f'Os valores digitados em ordem são {lista}')
print('='*80)

