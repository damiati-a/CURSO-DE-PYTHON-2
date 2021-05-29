# lista aleatoria preenhida por funções
# funções para sortear e para somar

from random import randint
from time import sleep


def sorteia(lista):
    for contador in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.2)
    print('FINISH HIM!')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares desta {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somapar(numeros)

