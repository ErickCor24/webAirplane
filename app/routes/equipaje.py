from flask import Blueprint,render_template,request,redirect,url_for
from utils.db import db
from models.equipaje import Equipaje


equipaje = Blueprint('equipaje', __name__, template_folder='templates',url_prefix='/equipaje')

@equipaje.route('/register',methods=['GET'])
def create():
    return render_template('views/equipaje/registro.html')

@equipaje.route('/', methods=['GET','POST'])
def register():
    if request.method=='POST':
        peso = request.form['peso']
        cantidad = request.form['cantidad']
        equipaje = Equipaje(peso,cantidad)
        db.session.add(equipaje)
        db.session.commit()

    return redirect(url_for('pasajero.register'))