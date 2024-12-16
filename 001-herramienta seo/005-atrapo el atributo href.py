import requests
from bs4 import BeautifulSoup

url = "https://elmundo.es/"
response = requests.get(url)
codigo = BeautifulSoup(response.text, 'html.parser')
enlaces = codigo.find_all('a')

for enlace in enlaces:
    print(enlace.get('href'))
