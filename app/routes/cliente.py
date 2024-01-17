from flask import Blueprint, render_template, request
from flask import flash, redirect, url_for



cliente = Blueprint('cliente', __name__, template_folder='templates',url_prefix='/cliente')


@cliente.route('/registro')

def registroCliente():
    return render_template('views/cliente/registro_cliente.html')




# @cliente.route('/', methods = ['GET','POST'])
# def store_passenger():
    






