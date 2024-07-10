from extensions import db  # Import the shared database instance

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

class House(db.Model):
    __tablename__ = 'houses'
    id = db.Column(db.Integer, primary_key=True)
    house_number = db.Column(db.String(20), nullable=False)
    street_name = db.Column(db.String(100), nullable=False)
    suburb = db.Column(db.String(100), nullable=False)
    postal_code = db.Column(db.String(10), nullable=False)
    geo_location = db.Column(db.String(50), nullable=False)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    initials = db.Column(db.String(10), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    second_name = db.Column(db.String(50))
    email = db.Column(db.String(100), nullable=False, unique=True)
    cell_number = db.Column(db.String(20), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    house_id = db.Column(db.Integer, db.ForeignKey('houses.id'))
    is_active = db.Column(db.Boolean, default=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.relationship('Role', backref=db.backref('users', lazy=True))
    house = db.relationship('House', backref=db.backref('users', lazy=True))

class Report(db.Model):
    __tablename__ = 'reports'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.Text)
    image_path = db.Column(db.String(255), nullable=False)
    geo_location = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    user = db.relationship('User', backref=db.backref('reports', lazy=True))

class PickupSchedule(db.Model):
    __tablename__ = 'pickup_schedules'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time_range = db.Column(db.String(50))

class Notification(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    is_read = db.Column(db.Boolean, default=False)
    user = db.relationship('User', backref=db.backref('notifications', lazy=True))
