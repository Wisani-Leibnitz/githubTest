from flask import render_template
from models import User  # Import the User model
from . import managers_bp  # Import the blueprint

@managers_bp.route('/')
def index():
    """Render the Managers app index page."""
    # Query users with the manager role
    managers = User.query.filter_by(role_id=2).all()
    return render_template('managers.html', managers=managers)
