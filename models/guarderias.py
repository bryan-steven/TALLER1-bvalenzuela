from db import db

class Guarderias(db.Model):
    __tablename__ = 'guarderias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(50), nullable=False)