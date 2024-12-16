import requests
from bs4 import BeautifulSoup
import sqlite3
import time

# Crear o conectar a una base de datos SQLite
db_name = "enlaces.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS enlaces (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    url TEXT
)
''')
conn.commit()

# URL inicial
url = "https://elmundo.es/"
response = requests.get(url)
codigo = BeautifulSoup(response.text, 'html.parser')
enlaces = codigo.find_all('a')

for enlace in enlaces:
    try:
        # Obtener el enlace
        url2 = enlace.get('href')
        if not url2 or not url2.startswith("http"):
            continue
        print(f"Procesando: {url2}")

        # Realizar una nueva solicitud para obtener el contenido del enlace
        response2 = requests.get(url2)
        codigo2 = BeautifulSoup(response2.text, 'html.parser')

        # Extraer el título de la página
        titulo = codigo2.title.string if codigo2.title else "Sin título"
        print(f"Título: {titulo}, URL: {url2}")

        # Insertar en la base de datos
        cursor.execute("INSERT INTO enlaces (titulo, url) VALUES (?, ?)", (titulo, url2))
        conn.commit()

        # Pausa para evitar sobrecarga del servidor
        time.sleep(5)

    except Exception as e:
        print(f"El enlace no se ha podido procesar: {e}")

# Cerrar conexión a la base de datos
conn.close()
