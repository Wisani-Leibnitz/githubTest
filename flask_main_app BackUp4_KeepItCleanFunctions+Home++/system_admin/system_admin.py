from flask import render_template
from . import system_admin_bp

@system_admin_bp.route('/')
def index():
    """Render the system admin index page."""
    return render_template('system_admin.html')
