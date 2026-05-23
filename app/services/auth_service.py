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