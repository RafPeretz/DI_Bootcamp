-- CREATE TABLE actors(
--  actor_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  age DATE NOT NULL,
--  number_oscars SMALLINT NOT NULL
-- )
-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Matt','Damon','08/10/1970', 5);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('George','Clooney','06/05/1961', 2);

-- ALTER TABLE actors RENAME COLUMN age TO birthdate;

-- SELECT * FROM actors;

-- CREATE TABLE movies(
-- movie_id SERIAL,
-- movie_title VARCHAR (50) NOT NULL,
-- movie_story TEXT,
-- actor_playing_id INTEGER,
-- PRIMARY KEY (movie_id),
-- FOREIGN KEY (actor_playing_id) REFERENCES actors (actor_id)
-- );

-- INSERT INTO movies (movie_title, movie_story, actor_playing_id) VALUES
--     ( 'Good Will Hunting', 
--     'Written by Affleck and Damon, the film follows 20-year-old South Boston janitor Will Hunting',
--     (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon')),
--     ( 'Oceans Eleven', 
--     'American heist film directed by Steven Soderbergh and written by Ted Griffin.', 
--     (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon'));


-- SELECT * FROM movies;

-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- INNER JOIN movies
-- ON actors.actor_id = movies.actor_playing_id;

-- CREATE TABLE producers(
-- producer_id SERIAL,
-- producer_name VARCHAR (50) NOT NULL,
-- movie_key_id INTEGER,
-- PRIMARY KEY (producer_id),
-- FOREIGN KEY (movie_key_id) REFERENCES movies (movie_id)
-- );



-- INSERT INTO producers (producer_name, movie_key_id)
-- VALUES('Jerry Weintraub',(SELECT movie_id from movies WHERE movie_title='Oceans Eleven'));


-- SELECT * FROM producers;

-- SELECT movies.movie_title,movies.movie_story, producers.producer_name
-- FROM movies
-- INNER JOIN producers
-- ON movies.movie_id = producers.movie_key_id;
