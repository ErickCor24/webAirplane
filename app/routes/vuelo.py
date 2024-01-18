from flask import Blueprint,render_template,request,redirect,url_for
from utils.db import db
from models.avion import Avion
from models.aeropuerto import Aeropuerto
from models.vuelo import Vuelo
from datetime import datetime,time

vuelo = Blueprint('vuelo', __name__, template_folder='templates',url_prefix='/vuelo')

@vuelo.route('/register')
def register():
    aviones= Avion.query.all()
    aeropuertos = Aeropuerto.query.all()
    return render_template('views/vuelo/register.html', aviones=aviones, aeropuertos=aeropuertos)

@vuelo.route('/', methods=['GET','POST'])
def store():
    if request.method == 'POST':
        fecha_salida = request.form['fecha_salida']
        hora_salida  = request.form['hora_salida']
        precio = request.form['precio']
        avion_id = request.form['avion_asignado']
        aeropuerto_id= request.form['aeropuerto_destino']

        try:
            vuelo = Vuelo(fecha_salida,hora_salida,precio,aeropuerto_id,avion_id)
            precio = float(precio)
            db.session.add(vuelo,)
            db.session.commit()
        except Exception as e:
            print(e)
    return redirect(url_for('vuelo.register'))

        

