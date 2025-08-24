# Write your MySQL query statement below

SELECT DISTINCT  user_id, 
       MAX(time_stamp) OVER (PARTITION BY user_id ORDER BY user_id ) AS last_stamp
FROM Logins
WHERE YEAR(time_stamp) = 2020;
