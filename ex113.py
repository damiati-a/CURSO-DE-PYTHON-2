# reescrever o programa e corrigir os erros do mesmo

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


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mPor favor. Digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados não fornecida pelo usuario\033[m')
            return 0
        else:
            return n


num1 = leiaInt('Digite um valor Inteiro: ')
num2 = leiaFloat('Digite um valor Real: ')
print(f'O valor digitado inteiro foi {num1} e o real foi {num2}')
