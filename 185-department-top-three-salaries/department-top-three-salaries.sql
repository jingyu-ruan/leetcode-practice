# Write your MySQL query statement below
SELECT d.name AS Department, 
       m.name AS Employee,
       m.salary AS Salary
FROM(
    SELECT e.*, # remember to add comma
    DENSE_RANK() OVER(PARTITION BY e.departmentId ORDER BY e.salary desc) AS rk
    FROM employee e
) m
LEFT JOIN Department d 
ON m.departmentId = d.id
WHERE m.rk <= 3;








