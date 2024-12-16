from flask import Flask, request, render_template, jsonify
import sqlite3
from flask_cors import CORS

aplicacion = Flask(__name__)
CORS(aplicacion, resources={r"/*": {"origins": "*"}})

@aplicacion.route('/')
def inicio():
    return render_template('index.html')

@aplicacion.route('/busca')
def busca():
    criterio = request.args.get('criterio', '')
    resultados = []

    if criterio:
        try:
            conn = sqlite3.connect("enlaces.db")
            cursor = conn.cursor()

            # Buscar en la base de datos usando LIKE
            cursor.execute("SELECT titulo, url FROM enlaces WHERE titulo LIKE ?", (f"%{criterio}%",))
            resultados = [{"titulo": row[0], "url": row[1]} for row in cursor.fetchall()]

            conn.close()
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify(resultados)

if __name__ == '__main__':
    aplicacion.run(debug=True, host='192.168.1.215', port=3000)
