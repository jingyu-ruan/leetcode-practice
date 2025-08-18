# Write your MySQL query statement below
SELECT MAX(num) AS num
FROM (SELECT CASE WHEN COUNT(*) =1 THEN MAX(num) END AS num
      FROM MyNumbers
      GROUP BY num ) t;


