# Write your MySQL query statement below
WITH wd AS (
    SELECT p.employee_id, review_date, rating, name, 
           ROW_NUMBER() OVER (PARTITION BY employee_id ORDER BY review_date DESC) AS rk
    FROM performance_reviews p
    LEFT JOIN employees e ON p.employee_id = e.employee_id 
), rk3 AS (
    SELECT *, 
           LEAD(rating, 1) OVER (PARTITION BY employee_id ORDER BY rk) AS rating_1, 
           LEAD(rating, 2) OVER (PARTITION BY employee_id ORDER BY rk) AS rating_2
    FROM wd
    # WHERE rk =1
)
SELECT employee_id, name, rating - rating_2 AS improvement_score
FROM rk3
WHERE rk=1 AND rating > rating_1 AND rating_1 > rating_2
ORDER BY improvement_score DESC, name
;