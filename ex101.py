# um programa com uma função voto()
# calculando a idade da pessoa e vendo se ela tem voto obrigatório, não precisa ou opicional


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPICIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


nascimento = int(input('Em que ano você nasceu: '))
print(voto(nascimento))
