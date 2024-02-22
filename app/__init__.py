from flask import Flask

import mysql.connector 


# db = list()
db = mysql.connector.connect( # LLAMAMOS AL FUNCION CONNECT PARA CONECTARNOS
    host ='localhost',
    port = 6333,
    ssl_disabled = True,
    user ='root', #USUARIO QUE USAMOS NOSOTROS
    password ='julia', #CONTRASEÑA CON LA QUE NOS CONECTAMOS
    database='JuliaGrishanova'
) 


def create_app():
    app = Flask(__name__)
    app.debug = True
    

    from .routes import routes
    from .routes import routes_autores


    app.register_blueprint(routes.rutas_libros)
    app.register_blueprint(routes_autores.rutas_autores)


    return app
