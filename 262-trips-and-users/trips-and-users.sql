SELECT request_at AS `Day`, 
       (ROUND(AVG(CASE WHEN status = 'cancelled_by_driver' OR status = 'cancelled_by_client' THEN 1 ELSE 0 END), 2)) AS `Cancellation Rate`
FROM Trips t
JOIN Users u1 ON u1.users_id = t.client_id
JOIN Users u2 ON u2.users_id = t.driver_id
WHERE u1.banned = 'No' AND u2.banned = 'No' AND request_at <= '2013-10-03'
GROUP BY request_at
;