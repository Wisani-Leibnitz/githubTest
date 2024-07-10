from flask import Blueprint

keep_it_clean_bp = Blueprint('keep_it_clean', __name__)

from . import keep_it_clean
