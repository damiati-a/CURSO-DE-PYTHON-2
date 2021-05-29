# print avançado
# comando de escrita utilizado atraves de funções personalizadas


def escreva(msg):
    tamanho = len(msg) + 4
    print('🇨🇳'*tamanho)
    print(f'  {msg}  ')
    print('🇨🇳'*tamanho)


escreva('ANDRÉZITO GOSTOZITO')
escreva('xablau')
escreva('vingador mais forte')
escreva = str(input('Digite uma mensagem: '))

