-- Find the top 2 films per category based on the number of rentals.
SELECT 
    c.name AS category,
    f.title,
    COUNT(r.rental_id) AS total_rentals
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
GROUP BY c.name, f.title
ORDER BY c.name, total_rentals DESC
LIMIT 2;
❌ Problem:
-- The LIMIT 2 applies globally, not per category.
-- You don’t get the top 2 films per category — you only get 2 films overall.

--   

SELECT category, title, total_rentals
FROM (
    SELECT 
        c.name AS category,
        f.title,
        COUNT(r.rental_id) AS total_rentals,
        RANK() OVER (PARTITION BY c.name ORDER BY COUNT(r.rental_id) DESC) AS film_rank
    FROM rental r
    JOIN inventory i ON r.inventory_id = i.inventory_id
    JOIN film f ON i.film_id = f.film_id
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category c ON fc.category_id = c.category_id
    GROUP BY c.name, f.title
) ranked_films
WHERE film_rank <= 2
ORDER BY category, film_rank;

-- CTE type of the query

WITH ranked_films AS (
    SELECT 
        c.name AS category,
        f.title,
        COUNT(r.rental_id) AS total_rentals,
        RANK() OVER (PARTITION BY c.name ORDER BY COUNT(r.rental_id) DESC) AS film_rank
    FROM rental r
    JOIN inventory i ON r.inventory_id = i.inventory_id
    JOIN film f ON i.film_id = f.film_id
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category c ON fc.category_id = c.category_id
    GROUP BY c.name, f.title
)
SELECT 
    category, 
    title, 
    total_rentals
FROM ranked_films
WHERE film_rank <= 2
ORDER BY category, film_rank;

