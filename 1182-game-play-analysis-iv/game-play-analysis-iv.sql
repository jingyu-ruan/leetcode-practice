# Write your MySQL query statement below
SELECT ROUND(
    AVG(
        a3.player_id IS NOT NULL 
    ), 2
) AS fraction 
FROM(
    SELECT a.player_id, MIN(a.event_date) AS first_date
    From Activity a
    GROUP BY player_id
) a2
LEFT JOIN Activity a3
ON a2.player_id = a3.player_id
AND DATEDIFF(a3.event_date, a2.first_date) = 1;





