from flask import Blueprint, render_template
from . import db

bp = Blueprint('lenguaje', __name__, url_prefix="/lenguajes")

@bp.route('/')
def idioma():
    consulta = """
        SELECT name FROM language  
        ORDER BY name ASC
    """

    con = db.get_db()
    res = con.execute(consulta)
    lista_lenguaje = res.fetchall()
    paginaLenguaje = render_template("lenguaje.html",
                              lenguajes=lista_lenguaje)
    return paginaLenguaje

