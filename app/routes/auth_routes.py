from flask import Blueprint
from app.controllers.auth_controller import signup

auth_bp = Blueprint('auth_bp', __name__)

# Signup Endpoint
auth_bp.route('/signup', methods=['POST'])(signup)