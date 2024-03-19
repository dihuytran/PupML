from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite database file
db = SQLAlchemy(app)

class Pickup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resistance = db.Column(db.Float)
    inductance = db.Column(db.Float)
    wire_type = db.Column(db.String(50))
    turn_count = db.Column(db.Integer)
