# Contando vogais em tuplas

palavras = ('Bonequinha', 'Pelotinha', 'Elegante', 'Magrelinha', 'Nega', 'Chinesa', 'Ninoso', 'Ninosa')
print(palavras)

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos --> ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')
