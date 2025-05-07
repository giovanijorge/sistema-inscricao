from . import db
from datetime import datetime

class Inscricao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    data_inscricao = db.Column(db.DateTime, default=datetime.utcnow)