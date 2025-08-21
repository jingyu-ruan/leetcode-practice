# Write your MySQL query statement below

WITH merge AS (
  SELECT
    s.student_id,
    s.student_name,
    sub.subject_name
  FROM Students s
  CROSS JOIN Subjects sub
)
SELECT
  m.student_id,
  m.student_name,
  m.subject_name,
  COUNT(e.subject_name) AS attended_exams
FROM merge m
LEFT JOIN Examinations e
  ON e.student_id = m.student_id
 AND e.subject_name = m.subject_name
GROUP BY
  m.student_id, m.student_name, m.subject_name
ORDER BY
  m.student_id, m.subject_name;




