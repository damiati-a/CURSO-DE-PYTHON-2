# Função para descobrir o maior valor
from time import sleep


def maior(* num):
    contador = maior = 0
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = maior
        contador += 1
    print(f'Foram informados {contador} valores ao todo')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 5, 7, 8, 0)
maior(1, 5, 2)
maior(7, 1000, 10001)
maior(1)

