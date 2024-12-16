import requests
from bs4 import BeautifulSoup

url = "https://elmundo.es/"
response = requests.get(url)
codigo = BeautifulSoup(response.text, 'html.parser')
enlaces = codigo.find_all('a')

for enlace in enlaces:
    print(enlace.get('href'))
    url2 = enlace.get('href')
    response2 = requests.get(url2)
    codigo2 = BeautifulSoup(response.text, 'html.parser')
    titulo = codigo2.title.string
    print(titulo,url2)
