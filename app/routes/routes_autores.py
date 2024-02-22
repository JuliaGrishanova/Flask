import random
from flask import Flask, Blueprint, render_template, request, redirect, url_for

from app import db
from app.data.autor_dao import AutorDAO
from app.data.modelo.autor import Autor

rutas_autores = Blueprint("routes_autores", __name__)

@rutas_autores.route('/verAutores')
def verAutores():
    autor_dao = AutorDAO()
    autores = autor_dao.select_all(db)
    return render_template('tabla_autores.html',autores=autores)



@rutas_autores.route('/addAutor', methods=['POST'])   
def addAutor():
    autor_dao = AutorDAO()
    autor = request.form['autor']
    pais = request.form['pais']
    ano = request.form['ano']
    if (autor == "" or pais == ""):
        return redirect(url_for('routes_autores.verAutores'))
    autor_dao.insert(db,autor,pais,ano)
    return redirect(url_for('routes_autores.verAutores'))    


@rutas_autores.route('/delAutor', methods=['POST'])   
def delAutor():
    autor_dao = AutorDAO()
    id = request.form['id']
    autor_dao.delete(db,id)
    return redirect(url_for('routes_autores.verAutores'))    

@rutas_autores.route('/updateAutor', methods=['POST'])   
def updateAutor():
    autor_dao = AutorDAO()
    id = request.form['id']
    autor = request.form['autor']
    pais = request.form['pais']
    ano = request.form['ano']
    autor_dao.update(db,id,autor,pais,ano)
    return redirect(url_for('routes_autores.verAutores'))    