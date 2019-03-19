from common.database import db_engine
from common.helpers import get_session
from models.recipe import Recipe
from models.recipe_ingredient import RecipeIngredient


def run_command(message, message_content):
    session = get_session()
    recipe_name = ' '.join(message_content.split(" ")[1:]) if len(message_content.split(" ")) > 1 else None
    if recipe_name:
        recipe = session.query(Recipe).filter(Recipe.name == recipe_name).first()
        if recipe:
            recipe_ingredients = session.query(RecipeIngredient).filter(RecipeIngredient.recipe_id == recipe.id).all()
            response = '__:newspaper2: Recipe For {}__'.format(recipe.name)
            for recipe_ingredient in recipe_ingredients:
                response += '\n{}({})'.format(recipe_ingredient.item.name, recipe_ingredient.item_amount)
        else:
            response = 'No recipe by that name was found.'
    else:
        recipes = session.query(Recipe).all()
        response = '__:newspaper2: Recipes __'
        for recipe in recipes:
            response += '\n{}'.format(recipe.name)

    return response
