from app.config.database import users_collection
from bson import ObjectId

# CREATE USER
def create_user(name, email, password, role):

    existing_user = users_collection.find_one({
        "email": email
    })

    if existing_user:
        return {
            "success": False,
            "message": "Email already exists"
        }

    new_user = {
        "name": name,
        "email": email,
        "password": password,
        "role": role
    }

    result = users_collection.insert_one(new_user)

    new_user["_id"] = str(result.inserted_id)

    return {
        "success": True,
        "message": "User registered successfully",
        "data": new_user
    }
def fetch_user(user_id):

    user = users_collection.find_one({
        "_id": ObjectId(user_id)
    })

    if not user:
        return {
            "success": False,
            "message": "User not found"
        }

    user["_id"] = str(user["_id"])

    return {
        "success": True,
        "data": user
    }
def modify_user(user_id, name, email, password, role):

    result = users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {
            "$set": {
                "name": name,
                "email": email,
                "password": password,
                "role": role
            }
        }
    )

    if result.matched_count == 0:
        return {
            "success": False,
            "message": "User not found"
        }

    updated_user = users_collection.find_one(
        {"_id": ObjectId(user_id)}
    )

    updated_user["_id"] = str(updated_user["_id"])

    return {
        "success": True,
        "message": "User updated successfully",
        "data": updated_user
    }
def remove_user(user_id):

    result = users_collection.delete_one(
        {"_id": ObjectId(user_id)}
    )

    if result.deleted_count == 0:
        return {
            "success": False,
            "message": "User not found"
        }

    return {
        "success": True,
        "message": "User deleted successfully"
    }

