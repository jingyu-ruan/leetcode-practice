# Write your MySQL query statement below

WITH m AS (
    SELECT employee_id, SUM(duration_hours) AS duration_hours, YEARWEEK(meeting_date, 1) AS week
    FROM meetings 
    GROUP BY employee_id, YEARWEEK(meeting_date, 1)
    HAVING duration_hours > 20
)
SELECT m.employee_id, employee_name, department, COUNT(*) AS meeting_heavy_weeks 
FROM m
LEFT JOIN employees e ON e.employee_id = m.employee_id
GROUP BY employee_id 
HAVING COUNT(*) >= 2
ORDER BY meeting_heavy_weeks DESC, e.employee_name
;