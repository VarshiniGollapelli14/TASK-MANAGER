from flask import request, jsonify
from app.services.auth_service import (
    create_user,
    fetch_user,
    modify_user,
    remove_user
)


def login():

    data = request.json

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    response = create_user(name, email, password)

    return jsonify(response)
#GET user
def get_user(id):
    response = fetch_user(id)
    return jsonify(response)
#update user
def update_user(id):
    data = request.json
    response = modify_user(
        id,
        data.get('name'),
        data.get('email'),
        data.get('password')
    )
    return jsonify(response)
#delete user
def delete_user(id):
    response = remove_user(id)
    return jsonify(response)
#signup endpoint
def signup():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')
    response = create_user(name, email, password, role)
    return jsonify(response)

def get_user(id):
    response = fetch_user(id)
    return jsonify(response)
def update_user(id):
    data = request.json
    response = modify_user(
        id,
        data.get('name'),
        data.get('email'),
        data.get('password'),
        data.get('role')
    )
    return jsonify(response)

def delete_user(id):
    response = remove_user(id)
    return jsonify(response)

    

    
