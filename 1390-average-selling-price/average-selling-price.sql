# Write your MySQL query statement below

WITH datematch AS  ( SELECT p.product_id, u.purchase_date, u.units, p.price
FROM  Prices p
LEFT JOIN UnitsSold u
ON u.product_id = p.product_id AND u.purchase_date BETWEEN p.start_date AND p.end_date  )

SELECT product_id, ROUND(IFNULL((SUM(units * price))/NULLIF(SUM(units), 0), 0), 2) 
       AS average_price 
FROM datematch
GROUP BY product_id;

