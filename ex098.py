# função para contador

from time import sleep


def contador(i, f, p):
    print('--'*50)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(2)

    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}, ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}, ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('--'*50)
print('Agora personalize uma contagem de sua maneira!')
inicio = int(input('INICIO: '))
fim = int(input('FIM: '))
passo = int(input('PASSO: '))
contador(inicio, fim, passo)
