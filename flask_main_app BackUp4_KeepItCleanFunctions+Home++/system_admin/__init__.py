from flask import Blueprint

system_admin_bp = Blueprint('system_admin', __name__)

from . import system_admin
