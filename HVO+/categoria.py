from flask import Blueprint, render_template
from . import db

bp = Blueprint('categoria', __name__, url_prefix="/categorias")

@bp.route('/')
def categoria():
    consulta = """
        SELECT name FROM category
        ORDER BY name ASC
    """

    con = db.get_db()
    res = con.execute(consulta)
    lista_categorias = res.fetchall()
    paginaCategoria = render_template("categoria.html",
                              categorias=lista_categorias)
    return paginaCategoria

