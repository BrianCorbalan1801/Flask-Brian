from flask import Blueprint, render_template
from . import db

bp = Blueprint('categoria', __name__, url_prefix="/categorias")

@bp.route('/')
def categoria():
    consulta = """
        SELECT name, category_id FROM category
        ORDER BY name ASC
    """

    con = db.get_db()
    res = con.execute(consulta)
    lista_categorias = res.fetchall()
    paginaCategoria = render_template("categoria.html",
                              categorias=lista_categorias)
    return paginaCategoria

@bp.route('/<int:id>')
def detalle(id):
    consulta = """
        SELECT name FROM category
        WHERE category_id = ?
    """

    con = db.get_db()
    res = con.execute(consulta, (id,))
    categoria = res.fetchone()
    consulta2 = """
        SELECT f.title as titulo, f.film_id FROM film f
        JOIN film_category fc on f.film_id = fc.film_id
        JOIN category c on fc.category_id = c.category_id
        WHERE c.category_id = ?
    """

    res = con.execute(consulta2, (id,))
    lista_peliculas = res.fetchall()
    paginaCategorias = render_template("detalles_categoria.html",
                                  categoria=categoria,
                                  pelis=lista_peliculas)
    return paginaCategorias