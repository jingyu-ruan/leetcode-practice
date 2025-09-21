# Write your MySQL query statement below
WITH m AS( 
    SELECT p1.product_id, category, user_id
    FROM ProductPurchases p1
    LEFT JOIN ProductInfo i ON i.product_id = p1.product_id 
), self_join AS (
    SELECT DISTINCT m1.user_id, 
        m1.category AS category1, 
        m2.category AS category2
        # COUNT(*) AS customer_count 
    FROM m m1
    JOIN m m2 ON m1.user_id = m2.user_id
    WHERE m1.category < m2.category
    # GROUP BY m1.category, m2.category
    # HAVING customer_count >=3 
)
SELECT category1, category2, COUNT(*) AS customer_count
FROM self_join
GROUP BY category1, category2
HAVING customer_count >=3 
ORDER BY customer_count DESC, category1, category2
;

