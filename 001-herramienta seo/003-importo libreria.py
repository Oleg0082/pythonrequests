import requests
from bs4 import BeautifulSoup

url = "https://elpais.com/"
response = requests.get(url)
codigo = BeautifulSoup(response.text, 'html.parser')
print(codigo.h2.string)
