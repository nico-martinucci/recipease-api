from flask import Flask
import os
from dotenv import load_dotenv
from routes.recipes import recipes
from routes.users import users

app = Flask(__name__)
app.register_blueprint(recipes, url_prefix="/api/recipes")
app.register_blueprint(users, url_prefix="/api/users")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ['DATABASE_URL'].replace("postgres://", "postgresql://"))
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
