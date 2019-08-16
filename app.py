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

app.config["MONGO_DBNAME"] = 'food_app'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

"Login Form"

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users =mongo.db.users
        login_user = users.find_one({'name' : request.form['username']})

        if login_user:
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for('index'))
            flash('Invalid username/password combination')
    return render_template('login.html')

"User Logout"

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

"User Registration Form"

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        flash('That username already exists! Please choose another')

    return render_template('register.html')

"Get all recipes"

@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

@app.route('/get_recipes')
def get_recipes():


"Add recipe form"

@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                            categories=mongo.db.category.find(),
                            allergens=mongo.db.allergen.find(),
                            preparation=mongo.db.preparation.find())


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
    recipes = mongo.db.recipes
    filter_with = {}
    exclude_allergen = ''

    category_name = request.form.get('category_name')
    if category_name is not None:
        filter_with['category_name'] = category_name

    allergen_name = request.form.get('allergen_name')
    if allergen_name is not None:
        filter_with['allergen_name'] = allergen_name

    exclude_allergen = request.form.getlist('allergen')
    if exclude_allergen is None:
        exclude_allergen = []

    recipes = recipes.find({'$and': [filter_with,
                         {'allergen': {'$nin': exclude_allergen}}]})

    return render_template('index.html', recipes=recipes, categories=mongo.db.category.find(),
                                   allergens=mongo.db.allergen.find())


"Recipes search"

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method=='POST':

        search_term = request.form.get("search_term")

        mongo.db.recipes.create_index( [("$**", 'text')] )

        cursor = mongo.db.recipes.find({ "$text": { "$search": search_term } })
        recipes = [recipe for recipe in cursor]

        return render_template('search.html', recipes=recipes, query=search_term)

        return render_template("search.html",
                                   recipes=recipes,
                                   categories=mongo.db.category.find(),
                                   allergen=allergens_mongo.db.category.find())

"Recipes search"

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method=='POST':

        search_term = request.form.get("search_term")

        mongo.db.recipes.create_index( [("$**", 'text')] )

        cursor = mongo.db.recipes.find({ "$text": { "$search": search_term } })
        recipes = [recipe for recipe in cursor]

        return render_template('search.html', recipes=recipes, query=search_term)

        return render_template("search.html",
                                   recipes=recipes,
                                   categories=mongo.db.category.find(),
                                   allergen=allergens_mongo.db.category.find())

if __name__ == "__main__":
    app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
