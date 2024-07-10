#from extensions import db  # Import the shared database instance
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class ManagersModel(db.Model):
    __tablename__ = 'managers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50))

    def __repr__(self):
        return f'<ManagersModel {self.name}>'
