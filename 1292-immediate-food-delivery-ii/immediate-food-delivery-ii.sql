# Write your MySQL query statement below

WITH firstorder AS (SELECT *, 
                ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS rk
                FROM Delivery d
                ),
                 rate AS (SELECT *, IF(order_date = customer_pref_delivery_date, 1, 0) AS immediate
FROM firstorder WHERE  rk =1)
SELECT ROUND(AVG(immediate)*100, 2) AS immediate_percentage
FROM rate

