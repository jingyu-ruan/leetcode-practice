# Write your MySQL query statement below

WITH neg AS (
    SELECT *, CASE WHEN operation = 'Buy' THEN -price 
              ELSE price END AS gl
    FROM Stocks
)

SELECT stock_name, SUM(gl) AS capital_gain_loss 
FROM neg
GROUP BY stock_name
ORDER BY operation_day;
