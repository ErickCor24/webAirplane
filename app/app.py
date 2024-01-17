from flask import Flask, render_template, request
from routes.cliente import cliente
from routes.equipaje import equipaje
from routes.pasajero import pasajero
from routes.vuelo import vuelo
from routes.boleto import boleto
from utils.db import db

app=Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = f'oracle+oracledb://system:oracle123@localhost:1521/xe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)



app.register_blueprint(cliente)
app.register_blueprint(equipaje)
app.register_blueprint(pasajero)
app.register_blueprint(vuelo)
app.register_blueprint(boleto)