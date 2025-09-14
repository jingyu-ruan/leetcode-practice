WITH first_date AS (
    SELECT customer_id, MIN(order_date) OVER (PARTITION BY customer_id) AS first_order, customer_pref_delivery_date, order_date
    FROM Delivery 
), is_immediate AS (
    SELECT *, CASE WHEN first_order = customer_pref_delivery_date THEN 1 ELSE 0 END AS same_day
    FROM first_date
    WHERE first_order = order_date 
)
SELECT ROUND(SUM(same_day) / COUNT(same_day) * 100, 2) AS immediate_percentage
FROM is_immediate
;