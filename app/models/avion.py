from sqlalchemy import Sequence
from utils.db import db

class Avion(db.Model):
    id = db.Column(db.String(7), primary_key=True)
    capacidad = db.Column(db.Integer, nullable=False)
    marca = db.Column(db.String(50), nullable=False)