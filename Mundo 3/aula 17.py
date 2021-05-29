# FUNÇÕES EM PYTHON

"""
FUNÇÕES = ROTINA
coisas que se faz constantemente dentro do python

# funções ja existentes no python
print(), int(), input(), float(), str()
-------------------------------------------------------------
"""
"""
Pode se criar uma função personalizada
tipo == mostralinha() => vai mostrar varias linhas ('-------------')
def mostralinha():
    print('------')
ao dar 
mostralinha() => o programa irá chamar a função def que foi criada
"""
"""

def mostralinha():
    print('-' * 10)
    
    
# precisa ter 2 linhas puladas após e antes da def para que esteja na formatação correta
print('oi')
mostralinha()
print('tchau')
mostralinha()
"""
"""
E é possivel criar def mais personalizadas para eventos semelhantes

def mensagem(msg):
    print('-')
    print(msg)
    print('-')
mensagem('Bom dia')
"""

"""
def titulo(txt):
    print('-'*20)
    print(txt)
    print('-'*20)


titulo('BOM DIA!')
titulo('BOA NOITE!')
"""

"""
def soma(a, b):
    s = a + b
    print(s)


# programa principal
soma(4, 5)
soma(a=8, b=9)
soma(1, 2)
soma(b=27, a=19)  # posso deixar explicito quais e onde serão meus valores
print()


# EMPACOTAMENTO
def contador(*num):  # o asterisco * faz com que o python jogue os valores dentro de um parametro independente de seus tamanhos
    for valor in num:
        print(f'{valor}', end='')
    print()
    tamanho = len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanho} números')


contador(1, 2, 3)
contador(0, 6, 7, 10)
"""


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [7, 2, 3, 29, -5]
dobra(valores)
print(valores)
