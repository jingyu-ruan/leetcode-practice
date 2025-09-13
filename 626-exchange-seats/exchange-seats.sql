# Write your MySQL query statement below
SELECT id, CASE WHEN MOD(id, 2)=0 THEN LAG(student, 1) OVER (ORDER BY id)
                WHEN MOD(id, 2)=1 AND id < MAX(id) OVER ()  THEN LEAD(student, 1) OVER (ORDER BY id)
                ELSE student END AS student
FROM seat
;