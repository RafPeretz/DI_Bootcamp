-- select * from items order by price desc;

-- -- Items with a price above 80 (80 included), ordered by price (highest to lowest).
--  select * from items where price<80 order by price desc;

-- -- -- The first 3 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
-- select  first_name,last_name from customers order by first_name,last_name limit 3;

-- -- -- All last names (no other columns!), in reverse alphabetical order (Z-A)
-- select last_name from customers order by last_name desc;

-- CREATE TABLE purchases (
--  customer_id INTEGER,
--  PRIMARY KEY (customer_id),
--  FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
	

--  );
-- create table purchases (
-- item_id integer,
-- FOREIGN KEY(item_id) REFERENCES public.items (item_id),
-- customer_id integer,
-- FOREIGN KEY(customer_id) REFERENCES public.customers (customer_id)
-- );

--  Insert into purchases(customer_id) values 
-- -- ((SELECT customer_id from customers WHERE first_name='Greg'));
-- SELECT * FROM purchases;
-- Insert into purchases(customer_id, item_id)values 
--  ((SELECT customer_id from customers WHERE first_name='Sandra'),(SELECT item_id from items WHERE price=300)),
-- ((SELECT customer_id from customers WHERE first_name='Scott'),(SELECT item_id from items WHERE price=80)),
-- --  ((SELECT customer_id from customers WHERE first_name='Trevor'),(SELECT item_id from items WHERE price=100)),
-- --  ((SELECT customer_id from customers WHERE first_name='Melanie'),(SELECT item_id from items WHERE price=300));
--  SELECT * FROM purchases;
--  -- not useful is only givung us the key 
 
--  select * from purchases inner join customers on purchases.customer_id = customers.customer_id;

-- select * from purchases inner join customers on purchases.customer_id = customers.customer_id where customers.customer_id=4;

-- Purchases for a large desk AND a small desk
-- select * from purchases inner join items on purchases.item_id = items.item_id where item_name='Small Desk' or item_name='Large Desk';

-- ------------------------------------------------------------------------------------------

-- -- -- 4. Create a purchase for Scott Scott – he bought a hard drive.-- --
-- Insert into customers(first_name, last_name) values ('Scott','Scott');
-- Insert into items(name,price) values('Hard Drive',200);
-- insert into purchases(customer_id , item_id) values
-- ((SELECT customer_id from customers WHERE first_name='Scott'),(SELECT items_id from items WHERE price=200));
