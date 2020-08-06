from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/widgethw'

db = SQLAlchemy(app)

class Widget(db.Model):
    __tablename__ = 'widgets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    wodget = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

    def __repr__(self):
        return f'🧙‍♀️ Widget(id={self.id}, name="{self.name}", wodget={self.wodget}, quantity={self.quantity}'

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "wodget": self.wodget,
            "qantity": self.quantity
        }