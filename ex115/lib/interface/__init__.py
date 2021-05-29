def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mPor favor. Digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados não fornecida pelo usuario\033[m')
            return 0
        else:
            return n


def linha(tam=40):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    contador = 1
    for item in lista:
        print(f'\033[33m{contador}\033[m - \033[35m{item}\033[m')
        contador += 1
    print(linha())
    opcao = leiaInt('Sua Opção: ')
    return opcao