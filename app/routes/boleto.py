from flask import Blueprint,render_template


boleto = Blueprint('boleto', __name__, template_folder='templates',url_prefix='/boleto')


@boleto.route('/register')
def register():
    return render_template('views/boleto/register.html')