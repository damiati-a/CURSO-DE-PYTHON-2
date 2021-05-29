# exibe na tela o fatorial utilizando um paramentro "show=True"


def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n:O número a ser calculado
    :param show: opcional - True para mostrar conta e False para não mostrar
    :return: O valor de fatorial do um número definido (n)
    """
    f = 1
    print(f'{n}! = ', end='')
    for c in range(n, 0, -1):
        if show:
            print(f' {c} ', end='')
            if c > 1:
                print('X', end='')
            else:
                print('=', end='')
        f *= c
    return f' {f}'


num = int(input('Digite um número para o fatorial: '))
resp = input('Deseja o calculo? [S/N]: ').strip().upper()[0]
if resp == 'S':
    show = True
else:
    show = False
print(fatorial(num, show))
