from sqlalchemy import Sequence
from utils.db import db

class Avion(db.Model):
    id = db.Column(db.Integer, Sequence('incrementidavion',start=1,increment=1),primary_key=True)
    capacidad = db.Column(db.Integer, nullable=False)
    marca = db.Column(db.String(50), nullable=False)