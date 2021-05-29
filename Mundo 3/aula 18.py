# FUNÇÕES PARTE 2
"""
- interactive help
- docstring
- argumentos opicionais
- escopo de variaveis
- retorno de resultados
"""
"""
INTERACTIVE HELP
help() - função interna
é um manual que contem dentro do python


print(input.__doc__)
help(input)
"""

'''
DOCSTRING


def contador(i, f, p):
    """
    :param i: INICIO DA CONTAGEM
    :param f: FIM DA CONTAGEM
    :param p: PASSO DA CONTAGEM
    :return: NÃO POSSUI RETORNO
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')


help(contador)
contador(0, 100, 10)
'''

"""
# PARAMETROS OPICIONAIS

def somar(a=0, b=0, c=0):  # ao receber 0 ele se torna um parametro opicional
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 9)
somar(1, 2)
somar(c=9, a=8)
"""

"""Escopo local só funcina quando declarado uma vez dentro de uma função.
Escopo global funciona quando declarado dentro de uma ou mais função."""

"""
def teste(b):
    global a  # so se a usa a variavel global ao se utilizar esta função (global)
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
    

a = 5
teste(a)
print(f'A fora vale {a}')
"""
"""RETORNANDO VALORES
 VARIAS SOMAS DE JEITOS DIFERENTES


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(7, 4)
r3 = somar(5)

print(f'os resultados foram {r1}, {r2}, {r3}')
"""

# PARTE PRÁTICA

"""
def fatorial(num = 1):
    f = 1
    for contador in range(num, 0, -1):
        f *= contador
    return f


f1 = fatorial(8)
f2 = fatorial(2)
f3 = fatorial()
print(f'O fatorial dos resultados são {f1}, {f2}, {f3}')

"""


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('PAR')
else:
    print('ÍMPAR')
