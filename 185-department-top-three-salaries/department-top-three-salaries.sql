WITH m AS (
    SELECT d.name AS Department, 
           e.name AS  Employee, 
           salary AS Salary,
           DENSE_RANK() OVER (PARTITION BY d.name ORDER BY salary DESC) AS rk
    FROM Employee e
    JOIN Department d ON d.id = e.departmentId 
)
SELECT Department, Employee, Salary
FROM m
WHERE RK <= 3
;





