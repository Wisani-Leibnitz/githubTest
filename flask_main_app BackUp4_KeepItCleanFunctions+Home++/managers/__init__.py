from flask import Blueprint

managers_bp = Blueprint('managers', __name__)

from . import managers
