from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

def test_call_all_entries(db_connection):
    db_connection.seed('seeds/recipes.sql')
    repository = RecipeRepository(db_connection)
    recipes = repository.all()
    assert recipes == [
        Recipe(1, "Cake", 30, 5),
        Recipe(2, "Pizza", 10, 1),
        Recipe(3, "Burger", 20, 3),
        Recipe(4, "Beans", 3, 2)
    ]
