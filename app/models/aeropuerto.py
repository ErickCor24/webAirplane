from sqlalchemy import Sequence
from utils.db import db

class Aeropuerto(db.Model):
    id = db.Column(db.Integer, Sequence('incrementidaeropuerto',start=1,increment=1),primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    ciudad = db.Column(db.String(50), nullable=False)
    pais = db.Column(db.String(20), nullable=False)
    