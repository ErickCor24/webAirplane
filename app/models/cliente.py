from sqlalchemy import Sequence
from utils.db import db

class Cliente(db.Model):
    id = db.Column(db.Integer, Sequence('incrementidcliente',start=1,increment=1),primary_key=True)
    nombre= db.Column(db.String(50), nullable=False)
    apellido= db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(50), nullable=False)


    def __init__(self, nombre, apellido, correo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono