users = []

def create_user(name, email, password):

    # Check duplicate email
    for user in users:
        if user['email'] == email:
            return {
                "success": False,
                "message": "Email already exists"
            }

    new_user = {
        "id": len(users) + 1,
        "name": name,
        "email": email,
        "password": password
    }

    users.append(new_user)

    return {
        "success": True,
        "message": "User registered successfully",
        "data": new_user
    }
#get user
def fetch_user(id):
    for user in users:
        if user['id'] == id:
            return {
                "success": True,
                "data": user
            }
    return {
        "success": False,
        "message": "User not found"
    }
#update user
def modify_user(id, name, email, password):
    for user in users:
        if user['id'] == id:
            user['name'] = name
            user['email'] = email
            user['password'] = password
            return {
                "success": True,
                "message": "User updated successfully",
                "data": user
            }
    return {
        "success": False,
        "message": "User not found"
    }
#delete user
def remove_user(id):
    for user in users:
        if user['id'] == id:
            users.remove(user)
            return {
                "success": True,
                "message": "User deleted successfully"
            }
    return {
        "success": False,
        "message": "User not found"
    }