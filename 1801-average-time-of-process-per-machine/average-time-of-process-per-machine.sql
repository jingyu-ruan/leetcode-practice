# Write your MySQL query statement below

WITH neg AS (
    SELECT *, 
    CASE WHEN activity_type = 'start' THEN - timestamp ELSE timestamp END 
    AS t
    FROM Activity 
)

SELECT machine_id, ROUND( SUM(t) / COUNT(t) * 2, 3 ) AS processing_time 
FROM neg
GROUP BY machine_id
;
