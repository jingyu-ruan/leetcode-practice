# Write your MySQL query statement below
WITH m AS (
    SELECT CASE WHEN MONTH(sale_date) IN (12, 1, 2) THEN 'Winter' 
                WHEN MONTH(sale_date) IN (3, 4, 5) THEN 'Spring'
                WHEN MONTH(sale_date) IN (6, 7, 8) THEN 'Summer'
                ELSE 'Fall' END AS season, 
        category, 
        SUM(quantity) AS total_quantity, 
        SUM(quantity * price) AS total_revenue
        # RANK() OVER (PARTITION BY season, category ORDER BY )
    FROM sales s
    LEFT JOIN products p ON s.product_id = p.product_id 
    GROUP BY season, category
), m2 AS (    
SELECT *, ROW_NUMBER() OVER (PARTITION BY season ORDER BY total_quantity DESC, total_revenue DESC, season) AS rk
FROM m
)
SELECT season, category, total_quantity, total_revenue
FROM m2
WHERE rk=1
;