# maior e menor valor de uma tupla

from random import randint

num = 0
valor = (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)),
(randint(1, 10)), (randint(1, 10))

print(f'Os valores sorteados foram: {valor} ', end='')
for n in valor:
    print(f'{n}', end='')
print(f'\nO maior valor sorteado foi {max(valor)}')
print(f'O menor valor sorteado foi {min(valor)}')

