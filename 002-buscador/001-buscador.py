from flask import Flask, request, render_template, jsonify
import json
from flask_cors import CORS

aplicacion = Flask(__name__)
CORS(aplicacion, resources={r"/*": {"origins": "*"}})

mensajes = []
@aplicacion.route('/')
def inicio():
    return render_template('index.html')
@aplicacion.route('/busca')
def busca():
    

if __name__ == '__main__':
    aplicacion.run(debug=True, host='192.168.1.215', port=3000)
