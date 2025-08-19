# Write your MySQL query statement below

SELECT product_id,
       year AS first_year,
       quantity,
       price
FROM (
    SELECT product_id, MIN(year) OVER (PARTITION BY product_id) AS min_year, quantity, price, year
    FROM Sales
) s
WHERE year = min_year;
-- GROUP BY product_id 
