from flask import Flask, render_template

app = Flask(__name__)

with app.app_context():
   from . import db
   db.init_app(app)

#Crea unas rutas sencillas
@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/quien')
def quien():
    return 'Hecho por Brian Corbalan!'

#Importa las bases de los archivos.py
from . import actores
app.register_blueprint(actores.bp)

from . import lenguajes
app.register_blueprint(lenguajes.bp)

from . import peliculas
app.register_blueprint(peliculas.bp)

from . import categoria
app.register_blueprint(categoria.bp)