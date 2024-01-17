from flask import Blueprint,render_template

equipaje = Blueprint('equipaje', __name__, template_folder='templates',url_prefix='/equipaje')

@equipaje.route('/register')
def registroEquipaje():
    return render_template('views/equipaje/registro.html')