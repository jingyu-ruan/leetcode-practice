SELECT e2.name
FROM Employee e1
JOIN Employee e2 ON e2.id  = e1.managerId 
GROUP BY e1.managerId 
HAVING COUNT(e1.managerId) >= 5
;