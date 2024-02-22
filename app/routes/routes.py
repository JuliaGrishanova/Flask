import random
from flask import Flask, Blueprint, render_template, request, redirect, url_for

from app import db
from app.data.autor_dao import AutorDAO
from app.data.libro_dao import LibroBIB
from app.data.modelo.autor import Autor

rutas_libros = Blueprint("routes", __name__)


@rutas_libros.route('/')
def index():
    return render_template('index.html')

@rutas_libros.route('/opiniones.html')
def opiniones():
    return render_template('opiniones.html')

@rutas_libros.route('/formulario')
def formulario():
    return render_template('formulario.html')



@rutas_libros.route('/verLibros', methods=['POST','GET'])
def verLibros():
    libros = list()
    autor_dao = AutorDAO()
    autores = autor_dao.select_all(db)

    libro_dao = LibroBIB()
    libros = libro_dao.select_all(db)
    return render_template('tabla.html',libros=libros,autores=autores)


@rutas_libros.route('/addLibro', methods=['POST'])   
def addLibro():
    libro_dao = LibroBIB()
    titulo = request.form['titulo']
    genero = request.form['genero']
    id_autor = request.form['id_autor']
 
    if (titulo == "" or genero == "" or id_autor == ""):
        return redirect(url_for('routes.verLibros'))

    libro_dao.insert(db,titulo,genero,id_autor)
    return redirect(url_for('routes.verLibros'))    

@rutas_libros.route('/delLibro', methods=['POST'])   
def delLibro():
    libro_dao = LibroBIB()
    id = request.form['id']
    libro_dao.delete(db,id)
   
    return redirect(url_for('routes.verLibros'))    


@rutas_libros.route('/updateLibro', methods=['POST'])   
def updateLibro():
    libro_dao = LibroBIB()
    id = request.form['id']
    titulo = request.form['titulo']
    genero = request.form['genero']
    if (titulo == "" or genero == "" ):
        return redirect(url_for('routes.verLibros'))
    libro_dao.update(db,id,titulo,genero)
   
    return redirect(url_for('routes.verLibros'))    