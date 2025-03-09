CREATE TABLE bears (
id: INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER,
sex TEXT CHECK(sex IN ('M', 'F')),
color TEXT,
temperament TEXT,
alive BOOLEAN

):