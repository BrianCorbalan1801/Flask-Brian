from flask import Blueprint, render_template
from . import db

bp = Blueprint('Peliculas', __name__, url_prefix="/peliculas")

@bp.route('/')
def pelicula():
    consulta = """
        SELECT title, film_id FROM film
        ORDER BY title ASC
    """

    con = db.get_db()
    res = con.execute(consulta)
    lista_Peliculas = res.fetchall()
    paginaPelicula = render_template("pelicula.html",
                              peliculas=lista_Peliculas)
    return paginaPelicula
