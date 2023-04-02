from flask import Flask
import os
from routes.recipes import recipes
from routes.users import users
from routes.ratings import ratings
from models import connect_db, db

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///recipease"
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = "SECREEEEEEEEEEEET"

connect_db(app)
db.create_all()

app.register_blueprint(recipes, url_prefix="/api/recipes")
app.register_blueprint(users, url_prefix="/api/users")
app.register_blueprint(ratings, url_prefix="/api/ratings")
