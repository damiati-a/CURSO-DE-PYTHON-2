# TRATAMENTO DE ERROS E EXEÇÕES
"""
print(x)  # erro de nome, variavel x nao foi definida

primt()  # erro de sintaxe, palavra escrita errada

n = int(input('numero: '))  # caso digite um valor contrario ao int, será um erro de valor

a = 9
b = 2
r = a / b
print(f'o resultado é {r}')  # caso divida por 0, dará um erro de divisão. Uma exeção.

r = 2 / '2'  # Erro de tipo, um numero dividindo por uma string, o programa nao entende como número

list = [3, 5, 2]
print(list[3])  # erro de indice, não existe o item 3 na lista, apenas 0, 1, 2
"""
"""
try:
    operação, o que pode dar problema
except:
    o que pode falhar no programa
else:
    caso de certo
finally: 
    vai ser usado dando certo ou não
"""
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('tivemos um problema ai em algo que foi digitado')
except ZeroDivisionError:
    print('Não é possivel dividir por 0')
except KeyboardInterrupt:
    print('O usuario nao digitou nada')
except Exception as error:
    print(f'O erro encontrado foi {error.__cause__}')
else:
    print(f'O resultado final é {r}')
finally:
    print('Valeu ai mermão')
