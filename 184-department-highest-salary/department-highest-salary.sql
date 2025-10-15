# Write your MySQL query statement below
WITH m AS (
    SELECT Department.name AS Department, 
           Employee.name AS Employee, 
           salary AS Salary, 
           DENSE_RANK() OVER (PARTITION BY Department.name ORDER BY salary DESC) AS rk
    FROM Employee
    JOIN Department ON Department.id = Employee.departmentId

)
SELECT Department, Employee, Salary
FROM m
WHERE rk = 1
;
