-- -- -- Get the average number of oscars in the table

-- -- SELECT avg(number_oscars) AS average_number_oscars FROM actors;

-- -- --Get distinct actors depending on their number of oscars
-- -- SELECT DISTINCT number_oscars FROM actors ORDER BY number_oscars ASC;

-- -- --Get the actors born after 01/01/1970
-- -- SELECT * FROM actors WHERE age <'01/01/1970';

-- -- --Get the actors which names are 'David', 'Morgan' or 'Will'
-- -- SELECT * FROM actors WHERE first_name in ('David','Morgan','Will');


-- -- UPDATE actors 
-- -- SET age='1980-01-02' 
-- -- WHERE first_name='Matt' AND last_name='Damon'
-- -- RETURNING 
-- --     actor_id,
-- --     first_name, 
-- --     last_name,
-- --     age;

-- -- DELETE FROM actors WHERE actor_id=3
-- -- RETURNING actor_id, first_name, last_name, number_oscars;

-- -- SELECT * FROM actors;

-- -- UPDATE actors 
-- -- SET age='1980-01-02' 
-- -- WHERE first_name='Matt' AND last_name='Damon'
-- -- RETURNING 
-- --     actor_id,
-- --     first_name, 
-- --     last_name,
-- --     age;



-- -- TRUNCATE TABLE actors RESTART IDENTITY;

-- -- ALTER TABLE actors ADD COLUMN children TEXT;

-- -- ALTER TABLE actors DROP COLUMN children;
-- --  ALTER TABLE actors RENAME COLUMN number_oscars TO number_cesars;
-- --  ALTER TABLE actors RENAME TO acteur;



-- -- SELECT * FROM acteur;

-- ALTER TABLE acteur
-- ALTER COLUMN number_cesars TYPE INT;
-- ALTER COLUMN last_name TYPE TEXT;

-- SELECT * FROM acteur;

DROP TABLE IF EXISTS acteur;

SELECT * FROM acteur;


