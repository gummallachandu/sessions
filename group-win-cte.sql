-- First: get total rentals per customer
WITH totals AS (
  SELECT customer_id, COUNT(*) AS total_rentals
  FROM rental
  GROUP BY customer_id
)
-- Then: join totals back to detail rows
SELECT
  r.rental_id,
  r.customer_id,
  r.rental_date,
  t.total_rentals
FROM rental r
JOIN totals t
  ON r.customer_id = t.customer_id
ORDER BY r.customer_id, r.rental_date;




✅ Window function version (cleaner)
SELECT
  r.rental_id,
  r.customer_id,
  r.rental_date,
  COUNT(*) OVER (PARTITION BY r.customer_id) AS total_rentals_for_customer
FROM rental r
ORDER BY r.customer_id, r.rental_date;


-- Keeps all rental rows.

-- Adds a new column showing the per-customer total rentals (same value repeated for each rental by that customer).


-- Using a derived table (subquery) instead of CTE
SELECT
  r.rental_id,
  r.customer_id,
  r.rental_date,
  t.total_rentals
FROM rental r
JOIN (
    SELECT customer_id, COUNT(*) AS total_rentals
    FROM rental
    GROUP BY customer_id
) t
  ON r.customer_id = t.customer_id
ORDER BY r.customer_id, r.rental_date;


GROUP BY version (needs join / subquery)

With plain GROUP BY, you lose the detail rows (rental_id, rental_date).
So you need to calculate totals in a subquery, then join back:

-- First: get total rentals per customer
WITH totals AS (
  SELECT customer_id, COUNT(*) AS total_rentals
  FROM rental
  GROUP BY customer_id
)
-- Then: join totals back to detail rows
SELECT
  r.rental_id,
  r.customer_id,
  r.rental_date,
  t.total_rentals
FROM rental r
JOIN totals t
  ON r.customer_id = t.customer_id
ORDER BY r.customer_id, r.rental_date;

-- 🔑 Key difference

-- GROUP BY alone collapses the rows — you can’t keep both detail (r.rental_id) and the aggregate (COUNT(*)) in the same query without extra work.

-- Window function lets you do it in one pass, no extra join or CTE.
