# Frostica
A role-playing game for discord which takes place on the continent of Frostica. Explore the land, craft, and survive. Overall, its a game about survival and does not follow the traditional RPG path of things such as treasure chests, monsters, shops, NPCs, etc. It's more about surviving in the land and crafting the things you need.

* Status (master): [![Build Status](https://travis-ci.com/FrostMiser/Frostica.svg?branch=master)](https://travis-ci.com/FrostMiser/Frostica)

## Player Commands (somewhat functional)
* !mine - Mine for stone and minerals in the area.
* !use <item> - Use an item in your inventory. This can be used for things such as eating food, drinking water, scribing
 spells, as well as equipping and unequipping items.
* !forage - Forage in the area for materials.
* !char - Show information about your character.
* !inv - Display your inventory.
* !craft <item> - Craft an item using items in your inventory.
* !chop - Chop trees in the area.
* !recipes - Display a list of crafting recipes.
* !map - Display the map of the area around you.
* !move <direction> - Move your character in a direction. Options are north, east, south, west.
* !equip <item> - Equip an item from your inventory.
* !hunt - Hunt for wild animals in the area.

## Player Commands (not complete)
* !enter - Attempt to enter the area of the map you are in (dungeons, houses, etc).
* !cast <spell> - Cast a spell in your spellbook.
* !spellbook - List the spells in your spellbook.

## Survival
To survive, you will need to find food and water. Eat food or drink water stored in your inventory with !use <item>. 
You will also need to stay warm in cold areas. Certain types of food also satisfy thirst.

### Hunger and Thirst
Hunger and thirst are affected by activities such as mining, chopping, and movement. Different types of terrain affect 
hunger and thirst differently.

## Admin Commands
* !setup - Setup the bot for first time use. This populates the database with items and recipes.


## Ideas for future version
* Claim land and build on it. Build a house and be able to enter it and put thing inside of it.
* Tame animals.
* Ride horses and dragons.
* Craft spells to add to the spellbook.
* Upgrade max mana, health, hunger, thirst (without adding levels).
* Require tools for mining and chopping trees, which can be upgraded and wear out when used.
* Underground map
* Temperatures, time of day, seasons
* Set a maximum inventory size and add ways to upgrade the size (bags, increase base size).
* Quests
* Spell Difficulty. Different spells are more or less difficult to cast.
* Spells
   - convert: Convert magic ore to mana.
   - teleport: Teleport up to 10 tiles away.
   - summon-food: Summons some food.
   - summon-water: Summons some water.
   - health-boost: Increases the players maximum health (temporarily or permanent)
   - mana-boost: Increases the players maximum mana (temporarily or permanent)
   - hunger-boost: Increases the players maximum hunger (temporarily or permanent)
   - thirst-boost: Increases the players maximum thirst (temporarily or permanent)
   - regenerate: Causes the players health to regenerate over time.
   - grow-tree: Grows trees in the tile the player is standing in.
 
 
