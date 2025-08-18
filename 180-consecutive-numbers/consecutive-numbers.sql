# Write your MySQL query statement below
# SELECT num AS ConsecutiveNums 
# FROM (
#     SELECT num, COUNT(*) 
#     FROM Logs 
#     GROUP BY num 
#     HAVING  COUNT(*) >= 3
# ) b;


# SELECT DISTINCT t.num AS ConsecutiveNums
# FROM (
#     SELECT num, CASE WHEN num = num-1 AND num = num+1 THEN TRUE
#     WHEN num = num-2 AND num = num-1 THEN TRUE
#     WHEN num = num+1 AND num = num+2 THEN TRUE
#     ELSE FALSE END AS consecutive
#     FROM Logs
#  t
# WHERE consecutive = TRUE

SELECT DISTINCT b.num AS ConsecutiveNums
FROM (
    SELECT num,
    LEAD(num, 1) OVER(ORDER BY id) AS lead1, 
    LEAD(num, 2) OVER(ORDER BY id) AS lead2
    FROM Logs
   
) b
WHERE num = lead1 AND num = lead2;
       




