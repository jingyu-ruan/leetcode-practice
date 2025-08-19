# Write your MySQL query statement below
SELECT p2.product_id,
       COALESCE(t.new_price, 10) AS price
FROM (SELECT DISTINCT product_id FROM Products) p2
LEFT JOIN (
    SELECT product_id, new_price
    FROM (
        SELECT product_id,
               new_price,
               ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rk
        FROM Products
        WHERE change_date <= '2019-08-16'
    ) x
    WHERE rk = 1
) t
ON p2.product_id = t.product_id;



