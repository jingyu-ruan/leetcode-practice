# Write your MySQL query statement below
WITH rate AS (
    SELECT user_id, 
           AVG(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) AS confirmation_rate
    FROM Confirmations
    GROUP BY user_id
)
SELECT s.user_id, ROUND(IFNULL(confirmation_rate, 0), 2) AS confirmation_rate
FROM Signups s
LEFT JOIN rate r ON r.user_id = s.user_id
;