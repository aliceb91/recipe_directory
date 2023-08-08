DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS books_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    recipe_name VARCHAR(255),
    cooking_time INTEGER,
    rating INTEGER
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Cake', 30, 5);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Pizza', 10, 1);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Burger', 20, 3);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Beans', 3, 2);
