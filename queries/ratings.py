from models import db, UserRecipe, Recipe
from statistics import mean


def check_user_recipe_activity(recipe_id, username):
    """
    Checks to see if the provided user has already interacted with the provided
    recipe. If they have, returns a reference to that interaction for 
    modification; if not, creates a new DB entry and returns that reference.
    Used for adding/deleting/modifying notes, starred status, made status, and 
    rating.
    """

    user_recipe_activity = UserRecipe.query.filter(
        UserRecipe.recipe_id == recipe_id,
        UserRecipe.user_username == username
    ).one_or_none()

    if not user_recipe_activity:
        new_activity = UserRecipe(
            user_username=username,
            recipe_id=recipe_id,
        )

        db.session.add(new_activity)
        db.session.commit()

        return new_activity

    return user_recipe_activity


def add_rating_to_recipe(recipe_id, username, rating):
    """
    Adds a rating record to the provided recipe; recalculates average rating and 
    updates the recipe's overall rating; returns the new overall rating.
    """

    user_recipe_activity = check_user_recipe_activity(
        recipe_id=recipe_id,
        username=username
    )

    user_recipe_activity.rating = rating
    db.session.commit()

    # calculate the new average rating for this recipe
    all_recipe_activity = UserRecipe.query.filter(
        UserRecipe.recipe_id == recipe_id
    ).all()

    mean_recipe_rating = mean([
        recipe.rating
        for recipe in all_recipe_activity
    ])

    rated_recipe = Recipe.query.get(recipe_id)
    rated_recipe.rating = mean_recipe_rating

    db.session.commit()

    serialized = {
        "recipe_id": rated_recipe.id,
        "rating": rated_recipe.rating,
    }

    return {"rating": serialized}
