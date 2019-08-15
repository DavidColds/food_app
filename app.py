from flask import Flask, render_template, redirect, request, url_for, session, flash, current_app
from flask_pymongo import PyMongo, DESCENDING
from bson.objectid import ObjectId
from pymongo import MongoClient
import re
import os
import bcrypt

app = Flask(__name__)

<<<<<<< HEAD
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
app.secret_key = os.getenv("SECRET_KEY")

=======
app.config["MONGO_DBNAME"] = 'food_app'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
>>>>>>> 291ed33fed4ddb04cd3797f075b3621cdec99614

mongo = PyMongo(app)

"Login Form"

@app.route('/login', methods=['POST', 'GET'])
def login():

"User Logout"

@app.route('/logout')
def logout():

"User Registration Form"

@app.route('/register', methods=['POST', 'GET'])
def register():

"Get all recipes"

@app.route('/get_recipes')
def get_recipes():


"Add recipe form"

@app.route('/add_recipe')
def add_recipe():


"Submit recipe to database"

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():


"Edit recipe form"

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):


"Submit edited recipe to database"
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):

"Delete recipe from database"

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):


"View full recipe"

@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):


@app.route('/')
@app.route('/recipes', methods=['GET', 'POST'])
def index():


"Recipes filter"

@app.route("/filter", methods=['GET', 'POST'])
def filter():


"Recipes search"

@app.route('/search', methods=['GET', 'POST'])
def search():

if __name__ == "__main__":
    app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
