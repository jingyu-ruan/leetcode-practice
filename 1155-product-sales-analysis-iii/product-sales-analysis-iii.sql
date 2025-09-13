# Write your MySQL query statement below
WITH first AS (
    SELECT *, MIN(year) OVER (PARTITION BY product_id) AS first_year
    FROM Sales
)

SELECT product_id, first_year, quantity, price
FROM first
WHERE first_year = year
;
