from sqlalchemy import Sequence
from sqlalchemy import Enum
from utils.db import db

class Boleto(db.Model):
    id= db.Column(db.Integer, Sequence('incrementidboleto',start=1,increment=1),primary_key=True)
    clase= db.Column(Enum('primera Clase','clase Ejecutiva','clase economica','clase economica premiun'), nullable=False)
    id_pasajero= db.Column(db.Integer, db.ForeignKey('pasajero.id'), nullable=False)
    id_vuelo= db.Column(db.Integer, db.ForeignKey('vuelo.id'), nullable=False)
    estado= db.Column(db.Boolean, nullable=False)
