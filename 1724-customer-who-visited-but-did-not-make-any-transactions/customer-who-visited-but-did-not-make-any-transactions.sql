# Write your MySQL query statement below

WITH mt AS (
    SELECT DISTINCT visit_id, transaction_id
    FROM Transactions
)

SELECT v.customer_id, SUM(CASE WHEN transaction_id IS NULL THEN 1 ELSE 0 END) AS count_no_trans
FROM Visits v
LEFT JOIN mt ON v.visit_id = mt.visit_id
GROUP BY customer_id
HAVING count_no_trans > 0;
