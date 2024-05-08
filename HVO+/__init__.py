from flask import Flask

app = Flask(__name__)

with app.app_context():
   from . import db
   db.init_app(app)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/quien')
def quien():
    return 'Hecho por Brian Corbalan!'