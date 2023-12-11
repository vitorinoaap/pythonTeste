# import urllib.request
#
# try:
#     site = urllib.request.urlopen('https://www.sapo.pt/')
# except urllib.request.URLError:
#     print('O Sapo não está acessível no momento')
# else:
#     print('Consegui abrir o Sapo com sucesso!')
#     print(site)
import webbrowser

new = 2
url = "https://categoriaoutros.com.br/?p=13819"  #ensina ambiente virtual

webbrowser.open(url, new=new)
