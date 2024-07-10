import os
import sys
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_migrate import Migrate  # Import Flask-Migrate
from models import db, User  # Ensure models is imported correctly

# Ensure the project directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Importing blueprints from other applications
from keep_it_clean import keep_it_clean_bp
from managers import managers_bp
from system_admin import system_admin_bp

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = '18403'  # Application secret key for session handling and flashing messages

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:18403@localhost/waste_management_system'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications to save resources

# Upload folder configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Initialize the database with the app
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Register blueprints for each app
app.register_blueprint(keep_it_clean_bp, url_prefix='/keep_it_clean')
app.register_blueprint(managers_bp, url_prefix='/managers')
app.register_blueprint(system_admin_bp, url_prefix='/system_admin')

@app.route('/')
def index():
    """Render the main index page."""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle the login functionality."""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email, password=password).first()
        
        if user:
            session['user_id'] = user.id
            session['role_id'] = user.role_id
            session['first_name'] = user.first_name
            
            if user.role_id in [1, 3, 5, 6]:  # Adjust roles based on your application
                return redirect(url_for('keep_it_clean.index'))
            elif user.role_id == 2:
                return redirect(url_for('managers.index'))
            elif user.role_id == 4:
                return redirect(url_for('system_admin.index'))
            else:
                flash('Unauthorized role.', 'error')
                return redirect(url_for('login'))
        else:
            flash('Invalid credentials, please try again.', 'error')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(port=5008, debug=True)
