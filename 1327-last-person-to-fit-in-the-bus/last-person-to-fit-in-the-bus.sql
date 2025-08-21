# Write your MySQL query statement below

WITH ordered AS (SELECT *, 
                 SUM(weight) OVER (ORDER BY Turn) AS `Total Weight`
                 FROM Queue
                 ORDER BY Turn)

SELECT person_name
FROM ordered
WHERE `Total Weight` <= 1000
ORDER BY turn DESC
LIMIT 1;
