
WITH id AS (
    SELECT DISTINCT product_id
    FROM Products 
), product_0816 AS (
    SELECT *, MAX(change_date) OVER (PARTITION BY product_id) AS latest
    FROM Products 
    WHERE change_date <= '2019-08-16'
), product_new AS (
    SELECT *
    FROM product_0816
    WHERE latest = change_date
)
SELECT id.product_id, IFNULL(p.new_price, 10) AS price
FROM id
LEFT JOIN product_new p ON id.product_id = p.product_id
;


