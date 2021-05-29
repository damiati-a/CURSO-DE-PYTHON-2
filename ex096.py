# um programa que tenha uma função area que mostre a area de um terreno

def titulo():
    print('-' * 20)
    print('CÁLCULO DE TERRENOS')
    print('-' * 20)


def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {a}m².')


titulo()
l = float(input('LARGURA(M): '))
c = float(input('COMPRIMENTO(M): '))
area(l, c)
