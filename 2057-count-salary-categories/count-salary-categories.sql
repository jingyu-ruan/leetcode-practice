# Write your MySQL query statement below

WITH c AS (
    SELECT *, 
       CASE WHEN income > 50000 THEN 'High Salary'
       WHEN income >= 20000 AND income <= 50000 THEN 'Average Salary'
       WHEN income < 20000 THEN 'Low Salary' END AS category
    FROM Accounts 
),

 l AS (
    SELECT 'High Salary' AS category
    UNION ALL SELECT 'Average Salary'
    UNION ALL SELECT 'Low Salary'
)

SELECT l.category, IFNULL(COUNT(c.category), 0) AS accounts_count
FROM l
LEFT JOIN c ON l.category = c.category
GROUP BY c.category
;


