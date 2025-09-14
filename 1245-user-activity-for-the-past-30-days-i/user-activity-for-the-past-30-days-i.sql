WITH unique_user AS (
    SELECT DISTINCT user_id, activity_date
    FROM Activity
)

SELECT activity_date AS day, COUNT(user_id) AS active_users
FROM unique_user
GROUP BY activity_date
HAVING activity_date >= DATE_SUB('2019-07-27', INTERVAL 29 DAY)
AND activity_date <= '2019-07-27'
;