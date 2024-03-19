from flask_sqlalchemy import SQLAlchemy

# Create SQLAlchemy instance without app context
db = SQLAlchemy()

class Pickup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resistance = db.Column(db.Float)
    inductance = db.Column(db.Float)
    wire_type = db.Column(db.String(50))
    turn_count = db.Column(db.Integer)

    def __repr__(self):
        return f"Pickup(id={self.id}, resistance={self.resistance}, inductance={self.inductance}, wire_type={self.wire_type}, turn_count={self.turn_count})"
