-- CREATE TABLE countries(
-- country_id  SERIAL,
-- coutry_name VARCHAR (50) NOT NULL
-- );

-- SELECT actors.first_name, actors.last_name, countries.coutry_name
-- FROM actors
-- INNER JOIN countries
-- ON actors.actor_id = countries.country_id;


-- SELECT actors.first_name, actors.last_name, countries.coutry_name
-- FROM actors
-- LEFT OUTER JOIN countries
-- ON actors.actor_id = countries.country_id;

-- SELECT actors.first_name, actors.last_name, countries.coutry_name
-- FROM actors
-- RIGHT OUTER JOIN countries
-- ON actors.actor_id = countries.country_id;

INSERT INTO countries(coutry_name)

-- SELECT actors.first_name, actors.last_name, countries.coutry_name
-- FROM actors
-- FULL OUTER JOIN countries
-- ON actors.actor_id = countries.country_id;
