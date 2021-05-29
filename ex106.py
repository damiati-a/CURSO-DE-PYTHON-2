# criando um sitema de ajuda interativa no Python

from time import sleep

cores = ('\033[m'  # 0 -> SEM CORES
         '\033[0;30;41m'  # 1 -> VERMELHO
         '\033[0;30;42m'  # 2 -> VERDE
         '\033[0;30;43m'  # 3 -> AMARELO
         '\033[0;30;44m'  # 4 -> AZUL
         '\033[0;30;45m'  # 5 -> ROXO
         '\033[7;30m'  # 6 -> BRANCO
         '')


def ajuda(com):
    titulo(f'\033[0;30;42mAcessando o manual do comando \'{comando}\'')
    print('\033[7;30m', end='')
    help(com)
    print('\033[m', end='')
    sleep(2)


def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(cores[cor], end='')
    print('-' * tamanho)
    print(f' {msg} ')
    print('-' * tamanho)
    print(cores[0], end='')
    sleep(2)


comando = ''
while True:
    titulo('\033[0;30;42mSITEMA DE AJUDA VOUTEAJUDEI.py')
    comando = str(input("Função ou biblioteca => "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('\033[0;30;45mOBRIGADO POR UTILIZAR NOSSA PLATAFORMA')
