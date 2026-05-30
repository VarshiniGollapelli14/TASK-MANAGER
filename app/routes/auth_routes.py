from flask import Blueprint
from app.controllers.auth_controller import (
    login,
    signup,
    get_user,
    update_user,
    delete_user
)

auth_bp = Blueprint('auth_bp', __name__)

# login Endpoint
auth_bp.route('/login', methods=['POST'])(login)

#get user
auth_bp.route('/users/<int:id>',methods=['GET'])(get_user)
#update user

auth_bp.route('/users/<int:id>',methods=['PUT'])(update_user)
#delete_user
auth_bp.route('/users/<int:id>',methods=['DELETE'])(delete_user)

#signup endpoint
auth_bp.route('/signup', methods=['POST'])(signup)

#get user
auth_bp.route('/signup/users/<int:id>',methods=['GET'])(get_user)

#update user
auth_bp.route('/signup/users/<int:id>',methods=['PUT'])(update_user)

#delete user
auth_bp.route('/signup/users/<int:id>',methods=['DELETE'])(delete_user)