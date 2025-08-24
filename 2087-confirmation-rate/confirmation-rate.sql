# Write your MySQL query statement below

WITH m AS (
    SELECT user_id,  
    AVG( CASE WHEN action = 'confirmed'THEN 1 ELSE 0 END ) AS confirmation_rate
    FROM Confirmations
    GROUP BY user_id
)

SELECT s.user_id, ROUND(IFNULL(m.confirmation_rate, 0), 2) AS confirmation_rate
FROM Signups s
LEFT JOIN m ON s.user_id = m.user_id
;



