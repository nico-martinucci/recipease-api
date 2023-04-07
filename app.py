from flask import Flask
from os import environ
from dotenv import load_dotenv
from routes.recipes import recipes
from routes.users import users
from routes.ingredients import ingredients
from models import connect_db, db

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///recipeats"
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = environ.get("SECRET_KEY")

connect_db(app)
db.create_all()

app.register_blueprint(recipes, url_prefix="/api/recipes")
app.register_blueprint(users, url_prefix="/api/users")
app.register_blueprint(ingredients, url_prefix="/api/ingredients")
