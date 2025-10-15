# Write your MySQL query statement below
WITH m AS (
    SELECT num, LAG(num, 1) OVER (ORDER BY id) AS log1, LAG(num, 2) OVER (ORDER BY id) AS log2
    FROM Logs
)
SELECT DISTINCT num AS ConsecutiveNums
FROM m 
WHERE num = log1 AND num = log2
;