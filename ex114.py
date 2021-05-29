# TESTANDO SE UM SITE ESTA ACESSÍVEL

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO site "Pudim.com.br" não está funcionando no momento\033[m')
else:
    print('\033[32mConsegui acessar o site "Pudim.com.br" com sucesso!\033[m')
    print(site.read)  # É possivel ler o conteúdo html do site
