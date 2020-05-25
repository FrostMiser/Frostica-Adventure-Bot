from common.helpers import get_session
from models.player_inventory import PlayerInventory
from models.recipe import Recipe
from models.recipe_ingredient import RecipeIngredient


def run_command(message, message_content):
    session = get_session()
    item_name = ' '.join(message_content.split(" ")[1:]) if len(message_content.split(" ")) > 1 else None

    if item_name:
        recipe = session.query(Recipe).filter(Recipe.name == item_name).first()
        if recipe:
            recipe_ingredients = session.query(RecipeIngredient).filter(
                RecipeIngredient.recipe_id == recipe.id).all()
            can_craft_item = True
            session.commit()
            for recipe_ingredient in recipe_ingredients:
                player_inventory_lookup = session.query(PlayerInventory).filter(
                    PlayerInventory.player_id == message.author.id,
                    PlayerInventory.item_id == recipe_ingredient.item_id,
                    PlayerInventory.item_amount >= recipe_ingredient.item_amount).first()
                if not player_inventory_lookup:
                    can_craft_item = False
                else:
                    if player_inventory_lookup.item_amount - recipe_ingredient.item_amount <= 0:
                        session.delete(player_inventory_lookup)
                    else:
                        player_inventory_lookup.item_amount = player_inventory_lookup.item_amount - \
                                                              recipe_ingredient.item_amount
            if can_craft_item:
                player_recipe_item = session.query(PlayerInventory).filter(
                    PlayerInventory.player_id == message.author.id, PlayerInventory.item_id == recipe.item_id).first()
                if player_recipe_item:
                    player_recipe_item.item_amount += 1
                else:
                    session.add(PlayerInventory(item=recipe.item, item_amount=1, player_id=message.author.id))
                session.commit()
                response = 'You craft a {}.'.format(recipe.name)
            else:
                response = 'You do not have one or more ingredients needed to craft that.'
                session.rollback()
        else:
            response = 'No recipe by that name was found.'
    else:
        response = 'You must say which item you want to craft with !craft <item>.'
    return response
