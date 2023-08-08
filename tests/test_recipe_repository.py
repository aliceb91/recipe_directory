from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

def test_call_all_entries(db_connection):
    # Given a seed of recipe data
    # It returns a list of all data from this seed.
    db_connection.seed('seeds/recipes.sql')
    repository = RecipeRepository(db_connection)
    recipes = repository.all()
    assert recipes == [
        Recipe(1, "Cake", 30, 5),
        Recipe(2, "Pizza", 10, 1),
        Recipe(3, "Burger", 20, 3),
        Recipe(4, "Beans", 3, 2)
    ]

def test_find_single_id(db_connection):
    # Given a recipe id
    # It returns the data for that recipe as a Recipe object.
    db_connection.seed('seeds/recipes.sql')
    repository = RecipeRepository(db_connection)
    recipe = repository.find(3)
    assert recipe == Recipe(3, "Burger", 20, 3)
