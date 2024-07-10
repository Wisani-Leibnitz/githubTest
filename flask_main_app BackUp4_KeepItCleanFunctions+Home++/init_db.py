from main_app import app
from extensions import db  # Import the db instance
from models import Role, House, User, Report, PickupSchedule, Notification  # Import all the models

# Create all tables in the database
with app.app_context():
    db.create_all()
    print("All tables created successfully.")
