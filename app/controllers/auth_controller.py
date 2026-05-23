from flask import request, jsonify
from app.services.auth_service import create_user

def signup():

    data = request.json

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    response = create_user(name, email, password)

    return jsonify(response)