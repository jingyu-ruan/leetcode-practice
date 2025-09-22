# Write your MySQL query statement below
WITH mean AS (
    SELECT t.driver_id, driver_name,
        CASE WHEN MONTH(trip_date) IN (1,2,3,4,5,6) THEN (distance_km / fuel_consumed) END AS first_half_avg, 
        CASE WHEN MONTH(trip_date) IN (7,8,9,10,11,12) THEN (distance_km / fuel_consumed) END AS second_half_avg
    FROM trips t
    LEFT JOIN drivers d ON t.driver_id = d.driver_id 
)
SELECT driver_id, driver_name, ROUND(AVG(first_half_avg), 2) AS first_half_avg, ROUND(AVG(second_half_avg), 2) AS second_half_avg, 
       ROUND(AVG(second_half_avg) - AVG(first_half_avg), 2) AS efficiency_improvement 
FROM mean
GROUP BY driver_id
HAVING (AVG(second_half_avg) - AVG(first_half_avg)) > 0
ORDER BY efficiency_improvement DESC, driver_name   
;