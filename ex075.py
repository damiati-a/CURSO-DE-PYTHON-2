# analise de dados com uma tupla
# quantas vezes aparecem o 9 e o 3

num = (int(input('Digite um número: '))), (int(input('Digite um número: '))), (int(input('Digite um número: '))), (int(input('Digite um número: '))), (int(input('Digite um número: ')))
print(f'você digitou os valor {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print(f'O valor 3 não foi digitado em nehuma posição')

for n in num:
    if n % 2 == 0:
        print(n, end=' ')

