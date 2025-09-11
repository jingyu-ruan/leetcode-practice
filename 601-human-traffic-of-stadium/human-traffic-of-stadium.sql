WITH bigger_than_100 AS(
    SELECT *
    FROM Stadium
    WHERE people >= 100
), 

consec AS(
    SELECT *, 
    LAG(id, 1)  OVER (ORDER BY id) AS prev1,
    LAG(id, 2)  OVER (ORDER BY id) AS prev2,
    LEAD(id, 1) OVER (ORDER BY id) AS next1,
    LEAD(id, 2) OVER (ORDER BY id) AS next2
    FROM bigger_than_100
)

SELECT id, visit_date, people 
FROM consec
WHERE (id+1 = next1 AND id+2 = next2)
OR (id+1 = next1 AND id-1 = prev1)
OR (id-2 = prev2 AND id-1 = prev1)
;