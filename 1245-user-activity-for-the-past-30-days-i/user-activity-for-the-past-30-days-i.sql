# Write your MySQL query statement below

SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity 
GROUP BY activity_date  
HAVING COUNT(DISTINCT user_id) > 0 
       AND activity_date >= DATE_SUB('2019-07-27', INTERVAL 29 DAY)
       AND activity_date <= '2019-07-27'