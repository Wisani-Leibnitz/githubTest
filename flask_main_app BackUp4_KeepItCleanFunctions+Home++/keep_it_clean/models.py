#from extensions import db  # type: ignore # Import the shared database instance
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class KeepItCleanModel(db.Model):
    __tablename__ = 'keep_it_clean'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))

    def __repr__(self):
        return f'<KeepItCleanModel {self.name}>'
