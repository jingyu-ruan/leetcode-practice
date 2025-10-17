WITH m AS (
    SELECT id, visit_date, people, 
        CASE WHEN people >= 100 THEN 1 ELSE 0 END AS is_100, 
        CASE WHEN LAG(people, 1) OVER (ORDER BY id) >= 100 THEN 1 ELSE 0 END AS lag1_is_100, 
        CASE WHEN LAG(people, 2) OVER (ORDER BY id) >= 100 THEN 1 ELSE 0 END AS lag2_is_100, 
        CASE WHEN LEAD(people, 1) OVER (ORDER BY id) >= 100 THEN 1 ELSE 0 END AS lead1_is_100, 
        CASE WHEN LEAD(people, 2) OVER (ORDER BY id) >= 100 THEN 1 ELSE 0 END AS lead2_is_100
    FROM Stadium
)
SELECT id, visit_date, people
FROM m
WHERE (is_100 = 1 AND lag1_is_100 = 1 AND lag2_is_100 = 1)
OR (is_100 = 1 AND lag1_is_100 = 1 AND lead1_is_100 = 1)
OR (is_100 = 1 AND lead1_is_100 = 1 AND lead2_is_100 = 1)
ORDER BY id

;