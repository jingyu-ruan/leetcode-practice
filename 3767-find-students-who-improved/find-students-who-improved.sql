WITH mm AS (
  SELECT
    student_id,
    subject,
    MIN(exam_date) AS first_date,
    MAX(exam_date) AS last_date
  FROM Scores
  GROUP BY student_id, subject
)
SELECT
  s1.student_id,
  s1.subject,
  s1.score AS first_score,
  s2.score AS latest_score
FROM mm
JOIN Scores s1
  ON s1.student_id = mm.student_id
 AND s1.subject    = mm.subject
 AND s1.exam_date  = mm.first_date
JOIN Scores s2
  ON s2.student_id = mm.student_id
 AND s2.subject    = mm.subject
 AND s2.exam_date  = mm.last_date
WHERE s2.score > s1.score
ORDER BY s1.student_id, s1.subject;
