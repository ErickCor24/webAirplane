from sqlalchemy import Sequence
from utils.db import db

class Pasajero(db.Model):
    id = db.Column(db.Integer, Sequence('incrementidpasajero',start=1,increment=1),primary_key=True)
    ci= db.Column(db.String(50), nullable=False, unique=True)
    nombre= db.Column(db.String(50), nullable=False)
    apellido= db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.Boolean, nullable=False)
    equipaje_id = db.Column(db.Integer, db.ForeignKey('equipaje.id'), nullable=False)

    def __init__(self,ci,nombre,apellido,telefono,correo,equipaje_id):
        self.ci = ci
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.estado = True
        self.equipaje_id = equipaje_id

