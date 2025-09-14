WITH order_count AS (
    SELECT buyer_id, COUNT(order_id) AS orders_in_2019 
    FROM Orders
    WHERE YEAR(order_date) = 2019
    GROUP BY buyer_id 
)
SELECT u.user_id AS buyer_id, u.join_date, IFNULL(oc.orders_in_2019, 0) AS orders_in_2019
FROM Users u
LEFT JOIN order_count oc ON oc.buyer_id = u.user_id
;

