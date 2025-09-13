# Write your MySQL query statement below
WITH rename_table AS(
    SELECT customer_id, product_key AS key1
    FROM Customer
),  product_cnt AS (
    SELECT customer_id,  COUNT(DISTINCT key1) AS cnt
    FROM rename_table c
    GROUP BY customer_id
    )

SELECT customer_id
FROM product_cnt
WHERE cnt = (SELECT COUNT(*) FROM Product)
;


