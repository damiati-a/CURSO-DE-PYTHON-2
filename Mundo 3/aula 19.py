# AULAS E PACOTES

"""
Modularização
Dividir um grande programa em pequenos pedaços

SIMPLIFICA-SE UM CÓDIGO UTILIZANDO OUTRO ARQUIVO.py
sendo assim se cria uma biblioteca personalizada em outro arquivo.
podendo importar um módulo que eu mesmo criei

"""
# from aula19_1 import fatorial, dobro, triplo
from aula19_uteis import numeros


num = int(input('Digite um número: '))
fat = aula19_uteis.fatorial(num)
print(f'O fatorial de {num}! é {fat}')
print(f'O dobre do valor {num} é {aula19_uteis.dobro(num)}, e o triplo é {aula19_uteis.triplo(num)}')
###########################################################################################

"""
vantagens de se usar modularização
- organização dos códigos
- facilidade na manutenção
- reuso em outros projetos
- ocultação de detalhamentos do código
"""
"""
PACOTES
uma pasta que contém módulos
separados por assuntos

"""

num = int(input('Digite um número: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num}! é {fat}')
print(f'O dobre do valor {num} é {numeros.dobro(num)}, e o triplo é {numeros.triplo(num)}')
###########################################################################################



