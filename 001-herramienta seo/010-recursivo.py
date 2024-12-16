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

def process_url(url, visited):
    if url in visited:
        return
    
    visited.add(url)
    print(f"Procesando: {url}")
    try:
        # Solicitar el contenido de la URL con timeout
        response = requests.get(url, timeout=5)
        codigo = BeautifulSoup(response.text, 'html.parser')

        # Extraer el título de la página
        titulo = codigo.title.string if codigo.title else "Sin título"
        print(f"Título: {titulo}, URL: {url}")

        # Insertar en la base de datos
        cursor.execute("INSERT INTO enlaces (titulo, url) VALUES (?, ?)", (titulo, url))
        conn.commit()

        # Encontrar todos los enlaces de la página
        enlaces = codigo.find_all('a')
        for enlace in enlaces:
            url2 = enlace.get('href')
            if url2 and url2.startswith("http"):
                process_url(url2, visited)
            

        # Pausa para evitar sobrecarga del servidor
        time.sleep(1)

    except Exception as e:
        print(f"El enlace no se ha podido procesar: {e}")

# URL inicial
url_inicial = "https://es.wikipedia.org/wiki/Directorio_web"
process_url(url_inicial, set())

# Cerrar conexión a la base de datos
conn.close()
