# Write your MySQL query statement below

WITH merged AS (
    SELECT user_id, IFNULL(SUM(distance), 0) AS travelled_distance 
    FROM Rides r
    GROUP BY user_id
)

SELECT u.name, IFNULL(merged.travelled_distance, 0) AS travelled_distance
FROM Users u 
LEFT JOIN merged ON u.id = merged.user_id
ORDER BY travelled_distance DESC, name;

