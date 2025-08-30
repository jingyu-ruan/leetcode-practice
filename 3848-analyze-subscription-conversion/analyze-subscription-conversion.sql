# Write your MySQL query statement below
WITH ft AS (
    SELECT user_id, AVG(activity_duration) AS trial_avg_duration 
    FROM UserActivity 
    WHERE activity_type = 'free_trial'
    GROUP BY user_id
), p AS (
    SELECT user_id, AVG(activity_duration) AS paid_avg_duration 
    FROM UserActivity 
    WHERE activity_type = 'paid'
    GROUP BY user_id
)

SELECT ft.user_id, ROUND(trial_avg_duration, 2) AS trial_avg_duration, ROUND(paid_avg_duration, 2) AS  paid_avg_duration
FROM ft
JOIN p ON ft.user_id = p.user_id
ORDER BY ft.user_id

;

