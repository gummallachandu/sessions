-- SUM() OVER → Running Total

-- Find cumulative revenue per customer.

SELECT 
    customer_id,
    payment_id,
    amount,
    SUM(amount) OVER (PARTITION BY customer_id ORDER BY payment_date) AS running_total
FROM payment
ORDER BY customer_id, payment_date;

SELECT 
    customer_id,
    rental_id,
    rental_date,
    ROW_NUMBER() OVER (
        PARTITION BY customer_id 
        ORDER BY rental_date
    ) AS rental_number,
    DATEDIFF(
        rental_date, 
        LAG(rental_date) OVER (
            PARTITION BY customer_id 
            ORDER BY rental_date
        )
    ) AS days_since_last_rental
FROM rental
ORDER BY customer_id, rental_number;

