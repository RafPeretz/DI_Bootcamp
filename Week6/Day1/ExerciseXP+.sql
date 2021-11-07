-- -- -- -- -- -- CREATE TABLE students(
-- -- -- -- -- --  id SERIAL PRIMARY KEY,
-- -- -- -- -- --  last_name VARCHAR (50) NOT NULL,
-- -- -- -- -- --  first_name VARCHAR (100) NOT NULL,
-- -- -- -- -- --  birth_date DATE NOT NULL
 
-- -- -- -- -- -- )

-- -- -- -- -- INSERT INTO students (last_name, first_name,birth_date)
-- -- -- -- -- VALUES
-- -- -- -- --  ('Benichou', 'Marc', '02/11/1998'),
-- -- -- -- --  ('Cohen', 'Yoan', '03/12/2010'),
-- -- -- -- -- 	('Benichou', 'Lea', '27/07/1987'),
-- -- -- -- -- 	('Dux', 'Amelia', '07/04/1996'),
-- -- -- -- -- 	('Grez', 'David', '14/06/2003'),
-- -- -- -- -- 	('Simpson', 'Omer', '03/10/1980');


-- -- -- -- -- SELECT * FROM students;

-- -- -- -- SELECT students last_name
-- -- -- -- FROM students;

-- -- -- SELECT * FROM students WHERE id = 2;


-- -- -- SELECT * FROM students WHERE last_name = 'Benichou ' and first_name ='Marc';

-- -- -- SELECT * FROM students WHERE last_name = 'Benichou ' OR first_name ='Marc';
-- -- -- SELECT * FROM students WHERE first_name LIKE '%a%';
-- -- SELECT * FROM students WHERE first_name like '%a';
-- -- SELECT * FROM students WHERE first_name is not like '%a';



-- SELECT * FROM students WHERE birth_date >='01/01/2000';



