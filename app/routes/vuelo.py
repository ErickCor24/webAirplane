from flask import Blueprint,render_template
from models.avion import Avion
from models.aeropuerto import Aeropuerto

vuelo = Blueprint('vuelo', __name__, template_folder='templates',url_prefix='/vuelo')

@vuelo.route('/register')
def register():
    aviones= Avion.query.all()
    aeropuertos = Aeropuerto.query.all()
    return render_template('views/vuelo/register.html', aviones=aviones, aeropuertos=aeropuertos)