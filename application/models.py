from application import db

# Таблица данных спутников
class Satellites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(125), nullable=False, unique=True)
    name = db.Column(db.String(125), nullable=False, unique=True)
    desc = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(125), nullable=False)
    target = db.Column(db.String(125), nullable=False)
    dataStart = db.Column(db.String(24), nullable=False)
    country = db.Column(db.String(125), nullable=False)
    massa = db.Column(db.Integer, nullable=False)
