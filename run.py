from app import app
from db import db

db.init_app(app)

@app.before_first_request #decorator affects the method below it,and runs the method before the first rqst
def create_table():
    db.create_all() #before the first request no matter which it is, it wil run this method to create data.db unless already exists
