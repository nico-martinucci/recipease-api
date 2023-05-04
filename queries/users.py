from models import User, UserRecipe, db
from flask_bcrypt import Bcrypt
import helpers.tokens as token
import queries.recipes as recipe_q

bcrypt = Bcrypt()


def add_new_user(username, email, password, first_name, last_name, bio):
    """
    Adds a new user to the database, returning a serialized dictionary if
    successful or error messages if not.
    """

    errors = []

    dupe_username = User.query.get(username)
    # TODO: does this work as .first()?
    dupe_email = User.query.filter(User.email == email).count()

    if dupe_username:
        errors.append("That username is already taken. Please try again.")

    if dupe_email:
        errors.append("That email is already taken. Please try again.")

    if errors:
        return {"error": errors}

    hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

    # try:
    new_user = User(
        username=username,
        email=email,
        password=hashed_pwd,
        first_name=first_name,
        last_name=last_name,
        bio=bio
    )

    db.session.add(new_user)
    db.session.commit()

    return {"token": get_user_jwt(username, new_user.is_verified)}

    # except:
    #     return {"error": "Something went wrong..."}


def authenticate_current_user(username, password):
    """
    Authenticates an existing user, returning a valid JWT if successful or
    error messages if not.
    """

    user = User.query.filter(User.username == username).first()

    if user:
        is_auth = bcrypt.check_password_hash(user.password, password)
        if not is_auth:
            return {"error": "Invalid username/password combination. Please try again."}

        return {"token": get_user_jwt(username, user.is_verified)}

    return {"error": "Username not found. Please try again."}


def get_user_jwt(username, is_verified):
    """
    Generates and returns a valid JWT with the provided username and 
    "isVerified" value.
    """

    return token.get_jwt(
        {
            "username": username,
            "isVerified": is_verified
        }
    )


def set_user_as_valid(email):
    """
    Sets a user's is_verified to true; used for new user email verification; 
    Returns the user's username for querying of more user data.
    """

    user = User.query.filter(User.email == email).one_or_none()

    user.is_verified = True

    db.session.commit()

    return user.username


def get_users(filter):
    """
    Queries and returns a list of all users, optionally filtered by the data
    passed to the function.
    """

    filter_term = "%{}%".format(filter)
    users = User.query.filter(User.username.ilike(filter_term)).all()

    serialized = [
        {
            "username": user.username,
            "firstName": user.first_name,
            "lastName": user.last_name,
            "photoUrl": user.photo_url
        }
        for user in users
    ]

    return {"users": serialized}


def get_user(username):
    """
    Queries and returns the full data for a particular user, including their
    posted recipes.
    """

    user = User.query.get(username)

    if not user:
        return {"error": "Invalid username. Please try again."}

    # TODO: flesh this out once there are routes to add recipes
    serialize_recipes = [
        {
            "id": recipe.id,
            "name": recipe.name,
            "description": recipe.description,
            "photoUrl": recipe.photo_url,
            "mealName": recipe.meal_name,
            "typeName": recipe.type_name,
            "createdBy": recipe.created_by.username,
            "rating": recipe.rating
        }
        for recipe in user.recipes
    ]

    serialize_user = {
        "username": user.username,
        "firstName": user.first_name,
        "lastName": user.last_name,
        "photoUrl": user.photo_url,
        "bio": user.bio,
        "recipes": serialize_recipes,
        "email": user.email,
        "favoritedRecipes": get_list_of_users_favorited_recipes(username=username).get("favoritedRecipes")
    }

    return {"user": serialize_user}


def get_list_of_users_favorited_recipes(username):
    """
    Gets and returns a list of recipe IDs that match the user's currently
    favorited recipes.
    """

    user_favorited_recipes = (UserRecipe.query
                              .filter(UserRecipe.user_username == username)
                              .filter(UserRecipe.is_starred == True)
                              )

    serialized = [
        activity.recipe_id
        for activity in user_favorited_recipes
    ]

    return {"favoritedRecipes": serialized}


def add_new_user_favorite(username, recipe_id):
    """
    Adds the provided recipe as a favorite for the provided user; uses the
    recipe method to determine existing interaction.
    """

    user_recipe_activity = recipe_q.check_user_recipe_activity(
        recipe_id=recipe_id,
        username=username
    )

    user_recipe_activity.is_starred = True
    db.session.commit()

    serialized = {
        "username": user_recipe_activity.user_username,
        "recipeId": user_recipe_activity.recipe_id,
        "isStarred": user_recipe_activity.is_starred
    }

    return {"favorited": serialized}


def remove_existing_user_favorite(username, recipe_id):
    """
    Removes an existing user favorite from the database.
    """

    user_recipe_activity = recipe_q.check_user_recipe_activity(
        recipe_id=recipe_id,
        username=username
    )

    user_recipe_activity.is_starred = False
    db.session.commit()

    serialized = {
        "username": user_recipe_activity.user_username,
        "recipeId": user_recipe_activity.recipe_id,
        "isStarred": user_recipe_activity.is_starred
    }

    return {"unfavorited": serialized}
