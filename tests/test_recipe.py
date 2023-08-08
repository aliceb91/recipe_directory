from lib.recipe import Recipe

def test_creates_recipe_entry():
    # Given recipie tablle data
    # Creates a Recipe object with the given data.
    recipe = Recipe(1, "Test", 10, 1)
    assert recipe.id == 1
    assert recipe.recipe_name == "Test"
    assert recipe.cooking_time == 10
    assert recipe.rating == 1

def test_returns_string_when_called():
    # Given a Recipe object
    # It returns a string containing it's data when called.
    recipe = Recipe(2, "Testing", 20, 5)
    result = str(recipe)
    assert result == "2, Testing, 20, 5"

def test_creates_comperable_objects():
    # Given a pair of Recipe objects
    # It accureately compares their contents.
    recipe_1 = Recipe(7, "Further testing", 17, 4)
    recipe_2 = Recipe(7, "Further testing", 17, 4)
    assert recipe_1 == recipe_2
