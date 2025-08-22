# Write your MySQL query statement below

SELECT p.product_name, SUM(o.unit) AS unit
FROM Orders o
LEFT JOIN Products p ON o.product_id = p.product_id
WHERE LEFT(o.order_date, 7) = '2020-02'  -- WHERE MONTH(order_date) = 2
GROUP BY o.product_id
HAVING SUM(o.unit) >= 100;

