WITH rank_date AS (
    SELECT *, 
        ROW_NUMBER() OVER (PARTITION BY student_id, subject ORDER BY exam_date) AS rk, 
        ROW_NUMBER() OVER (PARTITION BY student_id, subject ORDER BY exam_date DESC) AS rk_desc
    FROM Scores
)
SELECT student_id, subject, 
       MAX(CASE WHEN rk=1 THEN score END) AS first_score, 
       MAX(CASE WHEN rk_desc=1 THEN score END) AS latest_score 
FROM rank_date
GROUP BY student_id, subject
HAVING latest_score > first_score 
;