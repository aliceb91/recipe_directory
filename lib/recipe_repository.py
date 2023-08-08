from lib.recipe import Recipe

class RecipeRepository():
    def __init__(self, connection):
        # Establishes database connection on startup.
        self.connection = connection

    def all(self):
        # Pulls all available entries from table.
        rows = self.connection.execute('SELECT * FROM recipes')
        recipes = []
        for row in rows:
            item = Recipe(row["id"], row["recipe_name"], row["cooking_time"], row["rating"])
            recipes.append(item)
        return recipes
