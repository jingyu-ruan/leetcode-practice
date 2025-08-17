# Write your MySQL query statement below
SELECT Trips.request_at AS Day,
       ROUND(
        AVG(
            CASE
                WHEN Trips.status IN ('cancelled_by_driver', 'cancelled_by_client') THEN 1
                ELSE 0
            END
        ), 2
       ) AS 'Cancellation Rate'
FROM Trips
JOIN Users uc
    ON Trips.client_id = uc.users_id
    AND uc.banned = 'No'
JOIN Users ud
    ON Trips.driver_id = ud.users_id
    AND ud.banned = 'No'
WHERE Trips.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY Trips.request_at;