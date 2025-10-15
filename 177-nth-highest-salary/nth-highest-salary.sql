CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      WITH w AS (
        SELECT salary,
               DENSE_RANK() OVER (ORDER BY salary DESC) AS rk
        FROM Employee
      )
      SELECT MAX(CASE WHEN rk = N THEN salary END) 
      FROM w

  );
END