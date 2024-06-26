from flask import Blueprint, render_template
from . import db

bp = Blueprint('Peliculas', __name__, url_prefix="/peliculas")

@bp.route('/')
def pelicula():
    consulta = """
        SELECT title as titulo, film_id FROM film
        ORDER BY title ASC
    """

    con = db.get_db()
    res = con.execute(consulta)
    lista_Peliculas = res.fetchall()
    paginaPelicula = render_template("pelicula.html",
                              peliculas=lista_Peliculas)
    return paginaPelicula

@bp.route('/<int:id>')
def detalle(id):
    consulta = """
        SELECT title, rating, release_year, description, film_id FROM film
        WHERE film_id = ?
    """

    con = db.get_db()
    res = con.execute(consulta, (id,))
    pelicula = res.fetchone()
    consulta2 = """
        SELECT first_name, last_name, a.actor_id FROM film_actor fa
        JOIN actor a ON fa.actor_id = a.actor_id
        WHERE film_id = ?
    """

    res = con.execute(consulta2, (id,))
    lista_peliculas = res.fetchall()
    paginaPeliculas = render_template("detalles_peliculas.html",
                                  pelicula=pelicula,
                                  peliculas=lista_peliculas)
    return paginaPeliculas