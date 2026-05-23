from flask import Blueprint
from app.controllers.auth_controller import (
    login,
    get_user,
    update_user,
    delete_user
)

auth_bp = Blueprint('auth_bp', __name__)

# Signup Endpoint
auth_bp.route('/login', methods=['POST'])(login)

#get user
auth_bp.route('/users/<int:id>',methods=['GET'])(get_user)
#update user

auth_bp.route('/users/<int:id>',methods=['PUT'])(update_user)
#delete_user
auth_bp.route('/users/<int:id>',methods=['DELETE'])(delete_user)