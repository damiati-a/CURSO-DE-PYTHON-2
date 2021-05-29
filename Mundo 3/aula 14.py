# listas

"""
Diferente das tuplas as listas se usam [] ao invés de {}
e as listas são mutáveis. ou seja posso alterar meu código no meio de sua execução.

para se adicionar novos elementos ao final da lista se usa .append('')
ou na posição que quiser usando o .insert(0, '')

para apagar elementos se usa del ''[3]
ou o .pop(3)
ou .remove('')

"""
"""
outra coisa a se fazer com as listas é criar listas com o .range, como valores = list(range(4, 11))

ele cria uma lista com os valores de 4 até 10 conforme o indicado.

e para fora de ordem é só indicar na maneira que quer que os fique na lista.
se usar o valores.sort, os valores serão organizados.
para organizar ao contrário se usa valores. sort(reverse=True)

usando o len(valores) é possivel saber a quantidade de itens que tem na sua lista.

"""
"""
num = [2, 5, 8, 7]
num[2] = 3  # substitui os valores
num.append(1)  # acrescenta um número ao final da lista
num.sort()  # organiza em ordem
num.insert(2, 2)  # adiciona numeros no meio
num.pop(2)  # Elimina da lista
num.remove(2)  # elimina a primeira ocorrencia do valor solicitado
print(num)
print(f'Essa lista tem {len(num)} elementos')  # mostra quantos elementos tem na lista
"""
"""
valores = list()
for cont in range(0, 5):
    valores.append(int(input('digite um valor: ')))

for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}')
print('fim')
"""
a = [2, 3, 4, 5]
b = a[:]  # este simbolo significa que o b irá receber e copiar todos os valores do a
b[2] = 8
print(f'lista A: {a}')
print(f'Lista B: {b}')
