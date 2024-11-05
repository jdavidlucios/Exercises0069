INSERT INTO customer (first_name, last_name, email, address_id, active, create_date)
VALUES ('John', 'Doe', 'johndoe@example.com', 5, TRUE, CURRENT_DATE);

UPDATE customer
SET email = 'newemail@example.com'
WHERE customer_id = 1;

DELETE FROM customer
WHERE customer_id = 1;

INSERT INTO staff (first_name, last_name, email, store_id, active, username)
VALUES ('Jane', 'Smith', 'janesmith@example.com', 1, TRUE, 'jsmith');

UPDATE staff
SET email = 'newstaffemail@example.com'
WHERE staff_id = 2;

DELETE FROM staff
WHERE staff_id = 2;

INSERT INTO actor (first_name, last_name)
VALUES ('Chris', 'Evans');

UPDATE actor
SET last_name = 'Hemsworth'
WHERE actor_id = 3;

DELETE FROM actor
WHERE actor_id = 3;

SELECT rental.rental_id, rental.rental_date, customer.first_name, customer.last_name
FROM rental
JOIN customer ON rental.customer_id = customer.customer_id
WHERE EXTRACT(YEAR FROM rental.rental_date) = 2023
AND EXTRACT(MONTH FROM rental.rental_date) = 5;

SELECT payment.payment_id AS Número, payment.payment_date AS Fecha, payment.amount AS Total
FROM payment;

SELECT film.title, film.release_year, film.rental_rate
FROM film
WHERE film.release_year = 2006
AND film.rental_rate > 4.0;

