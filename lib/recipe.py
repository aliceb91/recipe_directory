class Recipe():
    def __init__(self, id, recipe_name, cooking_time, rating):
        # Accepts recipe data as parameters and stores them.
        #
        # Parameters:
        #   id: int
        #   recipe_name: string
        #   cooking_time: int
        #   rating: int
        self.id = id
        self.recipe_name = recipe_name
        self.cooking_time = cooking_time
        self.rating = rating

    def __repr__(self):
        # Returns the object contents as a string.
        return f"{self.id}, {self.recipe_name}, {self.cooking_time}, {self.rating}"

    def __eq__(self, other):
        # Compares object contents to that of another object.
        return self.__dict__ == other.__dict__
