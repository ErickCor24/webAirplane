from sqlalchemy import Sequence
from utils.db import db


class Vuelo(db.Model):
    id= db.Column(db.Integer, Sequence('incrementidvuelo',start=1,increment=1),primary_key=True)
    fecha_salida= db.Column(db.Date, nullable=False)
    hora_salida= db.Column(db.Time, nullable=False)
    precio= db.Column(db.Float, nullable=False)
    estado= db.Column(db.Boolean, nullable=False)
    id_aeropuerto_origen = db.Column(db.Integer, db.ForeignKey('aeropuerto.id'), nullable=False)
    id_avion = db.Column(db.Integer, db.ForeignKey('avion.id'), nullable=False)