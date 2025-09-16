# Write your MySQL query statement below
WITH daily_merge AS(
    SELECT customer_id, name, visited_on, SUM(amount) AS daily_amount
    FROM Customer
    GROUP BY visited_on
), cumsum AS 
    (SELECT visited_on, 
        SUM(daily_amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
        ROW_NUMBER() OVER (ORDER BY visited_on) AS rk
    FROM daily_merge)
SELECT visited_on, amount, ROUND(amount / 7, 2) AS average_amount
FROM cumsum
WHERE rk >= 7
;

