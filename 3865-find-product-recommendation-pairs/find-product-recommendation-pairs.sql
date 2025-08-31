# Write your MySQL query statement below
/*
WITH merged AS (
    SELECT pp.user_id, pp.product_id
    FROM ProductPurchases pp
    CROSS JOIN ProductPurchases pp2
    WHERE pp.user_id = pp2.user_id
)
*/
WITH merged AS (
    SELECT pp.user_id AS id1,
    pp.product_id AS product1_id,
    i.category AS product1_category,
    pp2.user_id AS id2,
    pp2.product_id AS product2_id,
    i2.category AS product2_category, 
    CONCAT(pp.product_id, pp2.product_id) AS cct, 
    COUNT(CONCAT(pp.product_id, pp2.product_id)) AS customer_count
    FROM ProductPurchases pp
    CROSS JOIN ProductPurchases pp2
    JOIN ProductInfo i ON i.product_id = pp.product_id
    JOIN ProductInfo i2 ON i2.product_id = pp2.product_id
    WHERE pp.user_id = pp2.user_id AND pp.product_id < pp2.product_id
    GROUP BY CONCAT(pp.product_id, pp2.product_id)
    HAVING customer_count >= 3
)

SELECT product1_id, product2_id, product1_category, product2_category, customer_count
FROM merged
ORDER BY customer_count DESC, product1_id, product2_id
;


