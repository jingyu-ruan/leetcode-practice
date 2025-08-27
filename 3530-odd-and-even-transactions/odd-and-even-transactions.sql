# Write your MySQL query statement below

WITH d AS (
    SELECT *,
           CASE WHEN MOD(amount, 2) = 1 THEN amount ELSE 0 END AS odd, 
           CASE WHEN MOD(amount, 2) = 0 THEN amount ELSE 0 END AS even
    FROM transactions
)

SELECT transaction_date, SUM(odd) AS odd_sum, SUM(even) AS even_sum
FROM d
GROUP BY transaction_date 
ORDER BY transaction_date 
;

