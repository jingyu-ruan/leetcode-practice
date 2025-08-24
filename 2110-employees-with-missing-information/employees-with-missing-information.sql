# Write your MySQL query statement below

WITH m AS (
SELECT employee_id
FROM Employees

UNION ALL

SELECT employee_id
FROM Salaries
)

SELECT employee_id FROM m
GROUP BY employee_id
HAVING COUNT(*) = 1
ORDER BY employee_id
;


