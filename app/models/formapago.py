from sqlalchemy import Sequence
from utils.db import db

class FormaPago(db.Model):
    id = db.Column(db.Integer, Sequence('incrementidformapago',start=1,increment=1),primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)