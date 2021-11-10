--Get a list of all film languages.
-- SELECT * FROM language;

-- SELECT title,description,language_id from film

-- SELECT film.title, film.description,language.name
-- FROM film
-- INNER JOIN language
-- ON film.language_id= language.language_id;

-- CREATE TABLE new_film(
--  id SERIAL PRIMARY KEY,
-- name_new_film VARCHAR (50) NOT NULL
-- )

-- INSERT INTO new_film(name_new_film) VALUES
-- ('Inception'),
-- ('Shutter Island'),
-- ('Titanic'),
-- ('Venom'),
-- ('Avengers End Game'),
-- ('Tenet')

-- SELECT * FROM new_film;



-- INSERT INTO customer_review(film_id,language_id,title,score,review_text,last_update) VALUES
-- ((SELECT film_id from film WHERE film_id = 54),
--  (SELECT language_id from language WHERE language_id = 1),
--   'Hey',
--   8,
--  'Superbe !!!',
--  '11/02/2003'
-- )
		
--  CREATE TABLE customer_review(
-- 	review_id SERIAL PRIMARY KEY,
--    film_id INTEGER REFERENCES new_film (id) ON DELETE RESTRICT,
--  	language_id  INTEGER REFERENCES language (language_id ) ON DELETE RESTRICT,
--  	title VARCHAR (50) NOT NULL,
--  	score INTEGER NOT NULL,
-- 	 CHECK(score > 0 and score < 11),
-- 	review_text VARCHAR (100) NOT NULL,
-- 	last_update DATE NOT NULL)
  
-- INSERT INTO customer_review(film_id,language_id,title,score,review_text,last_update) 
-- VALUES
-- ((SELECT id from new_film WHERE name_new_film = 'Titanic'),
--  (SELECT language_id from language WHERE language_id = 1),
--   'Titanic',  
--    9,
--   'RIP Jack !!!',
--   '11/02/2010'
--  )


-- SELECT * FROM customer_review;

-- DELETE FROM new_film WHERE id = 1


update language SET name = 'EN' where name='English' ;
update language SET name = 'FR' where name='French' ;
select name from language;

-- the foreign key in the customer table are address.
-- when i made an insert i have to check that the address id is in
-- the address table before insert element.
-- otherwise it will put an error.

-- to delete the customer_review table, we have to check all the
-- film in the new_film table that have a review.Then we can delete the review table.

select * from rental where return_date not in (select return_date from rental);

-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).

-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)

-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
select title from film,film_actor,actor where  film.film_id = film_actor.film_id
and film_actor.film_id = film.film_id
and description like '%sumo wrestler%' ;
-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.
select title from category,film_category,film where name='Documentary'
and length <60
and rating='R'
and category.category_id = film_category.category_id
and film.film_id = film_category.film_id;

-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental,
-- and he returned it between the 28th of July and the 1st of August, 2005.

select last_name from customer,payment,rental
where last_name='Matthew' and last_name='Mahan'
and amount='4.00'
and return_date between '2005-07-28' and '2005-08-28'
and rental.customer_id = customer.customer_id
and payment.rental_id = rental.rental_id;


-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat”
-- in the title or description, and it looked like it was a very expensive DVD to replace.





