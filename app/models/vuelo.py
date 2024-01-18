from sqlalchemy import Sequence
from sqlalchemy import Time
from sqlalchemy import Date
from utils.db import db


class Vuelo(db.Model):
    id= db.Column(db.Integer, Sequence('incrementidvuelo',start=1,increment=1),primary_key=True)
    fecha_salida= db.Column(db.String(10), nullable=False)
    hora_salida= db.Column(db.String(10), nullable=False)
    precio= db.Column(db.Float, nullable=False)
    id_aeropuerto_origen = db.Column(db.String(7), db.ForeignKey('aeropuerto.id'), nullable=False)
    id_avion = db.Column(db.String(7), db.ForeignKey('avion.id'), nullable=False)

    def __init__(self, fecha_salida, hora_salida, precio, id_aeropuerto_origen, id_avion):
        self.fecha_salida = fecha_salida
        self.hora_salida = hora_salida
        self.precio = precio
        self.id_aeropuerto_origen = id_aeropuerto_origen
        self.id_avion = id_avion