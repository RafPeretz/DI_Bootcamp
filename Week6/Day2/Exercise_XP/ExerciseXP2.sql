-- select * from customer;

-- select concat(first_name,' ',last_name) as full_name from customer;

-- select distinct create_date from customer;

-- select * from customer order by first_name desc;

-- select film_id, title, description ,release_year,rental_rate from film order by rental_rate asc;

-- select address, phone from address where district ='Texas';

-- select * from film where film_id >= 15 and film_id <= 150

-- SELECT film_id, title, description, rental_rate from film where title = 'Inception';

select film_id, title, description, length, rental_rate from film where title like 'In%';

select * from film order by rental_rate asc limit 10;

select * from film order by rental_rate asc limit 10 offset 10;

select payment.customer_id,amount, payment_date from payment inner join customer on payment.customer_id = customer.customer_id order by payment.customer_id;

-- 13.You need to check your inventory. Write a query to get all the movies which are not in inventory.
select * from film where film_id not in (select film_id from inventory);

--14.Write a query to find which city is in which country.
select city.city , country.country from city inner join country on country.country_id = city.country_id;

-- Write a query to get the customer’s id, names (first and last),
-- the amount and the date of payment ordered by the id of the staff member who sold them the dvd.
select staff.staff_id, customer.customer_id, customer.first_name, customer.last_name, amount, payment_date from customer
inner join payment on customer.customer_id = payment.customer_id
inner join staff on  staff.staff_id =payment.staff_id
order by staff_id;





