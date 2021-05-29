# variaveis composta (3 tipos)
# tuplas
# listas
# dicionario
"""
fatiamentos


lanche = tuple[hamburger][suco][pizza][pudim]
print(lanche[2]) = pizza
print(lanche[0:2] = pega do 0 ao 2
print(lanche[1:] = pega do suco até o final
print(lanche[-1] = pega o último elemento

for c in lanche:
    print(c)
    == cada vez que printar (c) irá mudar para o proximo

# tuplas são imutáveis, ou seja não são possiveis mudarem no meio do programa executado


"""
# pratica
"""
lanche = ('Hamburger', 'suco', 'pizza', 'pudim')
print(lanche)

for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]}')


for comida in lanche:
    print(f'eu vou comer {comida}')

for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posição {pos}')


# metodo organizado
print(sorted(lanche))

"""

a = (2, 5, 4)
b = (5, 8, 7, 2)
c = b + a
print(c.index(2, 1))

# pode se ter dados de tipos diferentes dentro de uma tupla, como str e numeros
