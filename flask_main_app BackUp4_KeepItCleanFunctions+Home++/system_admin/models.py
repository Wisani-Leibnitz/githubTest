#from extensions import db  # Import the shared database instance
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class SystemAdminModel(db.Model):
    __tablename__ = 'system_admin'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    admin_level = db.Column(db.Integer)

    def __repr__(self):
        return f'<SystemAdminModel {self.name}>'
