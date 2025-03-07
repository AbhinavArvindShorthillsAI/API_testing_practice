from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Create FastAPI instance
app = FastAPI()

# Dummy Database (List of Dictionaries)
users_db = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30},
]

# Pydantic Model for Full Update (PUT)
class User(BaseModel):
    name: str
    age: int

# Pydantic Model for Partial Update (PATCH)
class UpdateUserName(BaseModel):
    name: str  # Only the name field

# GET method - Fetch all users
@app.get("/users", response_model=List[dict])
def get_users():
    return users_db

# PATCH method - Update only the user's name
@app.patch("/users/{user_id}")
def update_user_name(user_id: int, user: UpdateUserName):
    for existing_user in users_db:
        if existing_user["id"] == user_id:
            existing_user["name"] = user.name  # Only update the name
            return existing_user
    raise HTTPException(status_code=404, detail="User not found")




 