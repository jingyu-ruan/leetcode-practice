# Write your MySQL query statement below

WITH m AS (
    SELECT *
    FROM Employees e
    LEFT JOIN (
        SELECT employee_id AS boss_id, name AS boss_name FROM Employees 
    ) r
    ON e.reports_to = r.boss_id
    WHERE e.reports_to > 0
)

SELECT boss_id AS employee_id, 
       boss_name AS name, 
       COUNT(reports_to) AS reports_count, 
       ROUND(AVG(age), 0) AS average_age
FROM m
GROUP BY reports_to  
ORDER BY employee_id 

;




