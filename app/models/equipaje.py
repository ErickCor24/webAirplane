from sqlalchemy import Sequence
from utils.db import db


class Equipaje(db.Model):
    id = db.Column(db.Integer, Sequence('incrementidequipaje',start=1,increment=1),primary_key=True)
    pesoTotal= db.Column(db.Integer, nullable=False)
    cantidadMaletas= db.Column(db.Integer, nullable=False)


    def __init__(self,pesoTotal,cantidadMaletas):
        self.pesoTotal = pesoTotal
        self.cantidadMaletas = cantidadMaletas
    