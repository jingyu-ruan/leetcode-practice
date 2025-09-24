# Write your MySQL query statement below

WITH m AS (
    SELECT customer_id, 
        COUNT(*) AS transaction_count, 
        MIN(transaction_date) AS registar_date, 
        MAX(transaction_date) AS final_date, 
        AVG(CASE WHEN transaction_type = 'refund' THEN 1 ELSE 0 END) AS refund_rate
    FROM customer_transactions 
    GROUP BY customer_id
)
SELECT customer_id 
FROM m
WHERE transaction_count >= 3
AND DATEDIFF(final_date, registar_date) >= 30
AND refund_rate < 0.2
;

