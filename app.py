from flask import Flask, Response, redirect
from flask_cors import CORS
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_basicauth import BasicAuth
from werkzeug.exceptions import HTTPException
from os import environ
from dotenv import load_dotenv
from routes.recipes import recipes
from routes.users import users
from routes.ingredients import ingredients
from routes.meals import meals
from routes.types import types
from routes.units import units
from routes.categories import categories
from models import (connect_db, db, User, Recipe, RecipeItem, RecipeStep,
                    RecipeComment, UserRecipe, RecipeIngredientSearch, RecipeType,
                    Ingredient, IngredientCategory, Meal, Unit, RecipeNote,
                    RecipePhoto)

load_dotenv()

app = Flask(__name__)
CORS(app)
basic_auth = BasicAuth(app)


class ModelView(ModelView):
    def __init__(self, model, *args, **kwargs):
        self.column_list = [c.key for c in model.__table__.columns]
        self.form_columns = self.column_list
        super(ModelView, self).__init__(model, *args, **kwargs)

    def is_accessible(self):
        if not basic_auth.authenticate():
            raise AuthException('Not authenticated.')
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(basic_auth.challenge())


class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("DATABASE_URI")
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = environ.get("SECRET_KEY")
app.config['BASIC_AUTH_USERNAME'] = environ["BASIC_AUTH_USERNAME"]
app.config['BASIC_AUTH_PASSWORD'] = environ["BASIC_AUTH_PASSWORD"]
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

admin = Admin(app)

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Recipe, db.session))
admin.add_view(ModelView(RecipeItem, db.session))
admin.add_view(ModelView(RecipeStep, db.session))
admin.add_view(ModelView(RecipeComment, db.session))
admin.add_view(ModelView(UserRecipe, db.session))
admin.add_view(ModelView(RecipeIngredientSearch, db.session))
admin.add_view(ModelView(RecipeType, db.session))
admin.add_view(ModelView(Ingredient, db.session))
admin.add_view(ModelView(IngredientCategory, db.session))
admin.add_view(ModelView(Meal, db.session))
admin.add_view(ModelView(Unit, db.session))
admin.add_view(ModelView(RecipeNote, db.session))
admin.add_view(ModelView(RecipePhoto, db.session))

connect_db(app)
db.create_all()
db.session.rollback()

app.register_blueprint(recipes, url_prefix="/api/recipes")
app.register_blueprint(users, url_prefix="/api/users")
app.register_blueprint(ingredients, url_prefix="/api/ingredients")
app.register_blueprint(meals, url_prefix="/api/meals")
app.register_blueprint(types, url_prefix="/api/types")
app.register_blueprint(units, url_prefix="/api/units")
app.register_blueprint(categories, url_prefix="/api/categories")
