from flask import Flask, render_template, redirect, url_for, request, flash
from connection import dbConnect
from client import client_page
from flight import vuelo_page
from boletPassengerFlight import boleto_page
from factura import factura_page

app = Flask (__name__)

app.register_blueprint(client_page)
app.register_blueprint(vuelo_page)
app.register_blueprint(boleto_page)
app.register_blueprint(factura_page)

rtnPasajero = None
vueloId = None


#Pagina de inicio Home
@app.route('/')
def index():
    return render_template('home.html')

#seccion de administracion de datos
@app.route("/administration")
def administration():
    return render_template('administrar.html')


if __name__ == '__main__':
    app.run(debug=True)
