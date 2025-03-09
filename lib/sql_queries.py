select_all_female_bears_return_name_and_age = """

CREATE TABLE bears (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    sex TEXT CHECK(sex IN ('M', 'F')),
    color TEXT,
    temperament TEXT,
    alive BOOLEAN
);

"""


select_all_bears_names_and_orders_in_alphabetical_order = """
INSERT INTO bears (name, age, sex, color, temperament, alive) VALUES
('Mr. Chocolate', 20, 'M', 'Brown', 'Calm', 1),
('Rowdy', 10, 'M', 'Black', 'Aggressive', 1),
('Tabitha', 6, 'F', 'Gray', 'Playful', 1),
('Sergeant Brown', 12, 'M', 'Brown', 'Serious', 1),
('Melissa', 13, 'F', 'Black', 'Gentle', 1),
('Grinch', 2, 'M', 'White', 'Grumpy', 1),
('Wendy', 6, 'F', 'Brown', 'Curious', 1),
(NULL, 8, 'M', 'Black', 'Mysterious', 1);"""


select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
SELECT name, age FROM bears WHERE alive = 1 ORDER BY age ASC;
"""

select_oldest_bear_and_returns_name_and_age = """
SELECT name, age FROM bears ORDER BY age DESC LIMIT 1;
"""

select_youngest_bear_and_returns_name_and_age = """
SELECT name, age FROM bears ORDER BY age ASC LIMIT 1;"""
