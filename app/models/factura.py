from sqlalchemy import Sequence
from utils.db import db

class Factura(db.Model):
    id = db.Column(db.Integer, Sequence('incrementidfactura',start=1,increment=1),primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    id_vuelo= db.Column(db.Integer, db.ForeignKey('vuelo.id'), nullable=False)
    id_forma_pago= db.Column(db.Integer, db.ForeignKey('formapago.id'), nullable=False)
    total= db.Column(db.Float, nullable=False)
    estado= db.Column(db.Boolean, nullable=False)