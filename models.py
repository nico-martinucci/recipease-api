from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    app.app_context().push()
    db.app = app
    db.init_app(app)


class User(db.Model):
    __tablename__ = "users"

    username = db.Column(db.Text, primary_key=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    bio = db.Column(db.Text)

    recipe_activity = db.relationship(
        "Recipe",
        secondary="users_recipes",
        backref="user_activity"
    )


class Recipe(db.Model):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_username = db.Column(db.Text, db.ForeignKey("users.username"))
    meal_name = db.Column(db.Text, db.ForeignKey("meals.name"), nullable=False)
    type_name = db.Column(
        db.Text,
        db.ForeignKey("recipe_types.name"),
        nullable=False
    )
    private = db.Column(db.Boolean, nullable=False)
    photo_url = db.Column(db.Text)

    created_by = db.relationship("User", backref="recipes")
    meal_category = db.relationship("Meal", backref="recipes")
    recipe_type = db.relationship("RecipeType", backref="recipes")


class RecipeItem(db.Model):
    __tablename__ = "recipe_items"

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(
        db.Integer,
        db.ForeignKey("recipes.id"),
        nullable=False
    )
    order = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    short_unit = db.Column(db.Text, db.ForeignKey("units.short"))
    ingredient = db.Column(
        db.Text,
        db.ForeignKey("ingredients.name"),
        nullable=False
    )
    description = db.Column(db.Text)

    recipe = db.relationship("Recipe", backref="items")
    unit = db.relationship("Unit")
    ingredient_detail = db.relationship("Ingredient", backref="uses")


class RecipeStep(db.Model):
    __tablename__ = "recipe_steps"

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(
        db.Integer,
        db.ForeignKey("recipes.id"),
        nullable=False
    )
    order = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    recipe = db.relationship("Recipe", backref="steps")


class RecipeComment(db.Model):
    __tablename__ = "recipe_comments"

    id = db.Column(db.Integer, primary_key=True)
    user_username = db.Column(
        db.Text,
        db.ForeignKey("users.username"),
        nullable=False
    )
    recipe_id = db.Column(
        db.Integer,
        db.ForeignKey("recipes.id"),
        nullable=False
    )
    comment = db.Column(db.Text, nullable=False)
    time_stamp = db.Column(db.DateTime, nullable=False)

    posted_by = db.relationship("User", backref="comments")
    recipe = db.relationship("Recipe", backref="comments")


class UserRecipe(db.Model):
    __tablename__ = "users_recipes"

    id = db.Column(db.Integer, primary_key=True)
    user_username = db.Column(
        db.Text,
        db.ForeignKey("users.username"),
        nullable=False
    )
    recipe_id = db.Column(
        db.Integer,
        db.ForeignKey("recipes.id"),
        nullable=False
    )
    notes = db.Column(db.Text)
    is_starred = db.Column(db.Boolean)
    is_made = db.Column(db.Boolean)
    rating = db.Column(db.Text)


class RecipeIngredientSearch(db.Model):
    __tablename__ = "recipes_ingredients_search"

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(
        db.Integer,
        db.ForeignKey("recipes.id"),
        nullable=False
    )
    ingredient_name = db.Column(
        db.Text,
        db.ForeignKey("ingredients.name"),
        nullable=False
    )


class RecipeType(db.Model):
    __tablename__ = "recipe_types"

    name = db.Column(db.Text, primary_key=True)
    description = db.Column(db.Text, nullable=False)


class Ingredient(db.Model):
    __tablename__ = "ingredients"

    name = db.Column(db.Text, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(
        db.Text,
        db.ForeignKey("ingredient_categories.name"),
        nullable=False
    )
    photo_url = db.Column(db.Text)

    category_detail = db.relationship(
        "IngredientCategory", backref="ingredients")
    recipes = db.relationship("RecipeItem")


class IngredientCategory(db.Model):
    __tablename__ = "ingredient_categories"

    name = db.Column(db.Text, primary_key=True)
    description = db.Column(db.Text, nullable=False)


class Meal(db.Model):
    __tablename__ = "meals"

    name = db.Column(db.Text, primary_key=True)
    description = db.Column(db.Text, nullable=False)

    def serialize(self):
        return {
            "name": self.name,
            "description": self.description
        }


class Unit(db.Model):
    __tablename__ = "units"

    short = db.Column(db.Text, primary_key=True)
    singular = db.Column(db.Text, nullable=False)
    plural = db.Column(db.Text, nullable=False)
