from fastapi import FastAPI, HTTPException
from typing import Optional

# Create FastAPI instance
app = FastAPI()

# Dummy Database (List of Dictionaries)
users_db = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30},
]

# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}

# GET method - Fetch all users
@app.get("/users")
def get_users():
    return users_db

#  GET method with Path Parameter
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

#  GET method with Query Parameters
@app.get("/search")
def search_users(name: Optional[str] = None, min_age: Optional[int] = None):
    results = users_db
    if name:
        results = [user for user in results if user["name"].lower() == name.lower()]
    if min_age:
        results = [user for user in results if user["age"] >= min_age]
    return results

# POST method - Create a new user 
@app.post("/users")
def create_user(name: str, age: int):
    new_id = len(users_db) + 1
    new_user = {"id": new_id, "name": name, "age": age}
    users_db.append(new_user)
    return new_user

