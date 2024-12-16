import requests

url = "https://jocarsa.com"
response = requests.get(url)
codigo = response.text
print(codigo)
