# um sitema de menu e cadastro modularizado
from lib.arquivo import *
from lib.interface import *
from time import sleep

arquivo = 'Sistema.txt'
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['VER CADASTRO DAS PESSOAS', 'CADASTRAR NOVAS PESSOAS', 'SAIR DO SISTEMA'])
    if resposta == 1:
        lerArquivo(arquivo)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        print('Finalizando o sitema.', end=''), sleep(0.5), print('.', end=''), sleep(0.5), print('.')
        break
    else:
        print('!ERRO! Digite uma opção válida!')
    sleep(2)
