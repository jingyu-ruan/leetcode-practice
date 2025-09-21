# Write your MySQL query statement below
WITH first_pos AS (
    SELECT patient_id, test_date, result, 
           ROW_NUMBER() OVER (PARTITION BY patient_id ORDER BY test_date) AS rk
    FROM covid_tests 
    WHERE result = 'Positive'
), first_neg AS (
    SELECT c.patient_id, 
           c.test_date AS neg_date, 
           c.result AS result2, 
           fp.test_date AS pos_date, 
           fp.result AS result1
    FROM covid_tests c
    JOIN first_pos fp ON c.patient_id = fp.patient_id
    WHERE c.result = 'Negative' AND rk = 1 AND c.test_date > fp.test_date
), first_neg2 AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY patient_id ORDER BY neg_date) AS rk2
    FROM first_neg
)
SELECT fn.patient_id, patient_name, age, 
       DATEDIFF(neg_date, pos_date) AS recovery_time 
FROM first_neg2 fn
LEFT JOIN patients p ON fn.patient_id = p.patient_id 
WHERE rk2 = 1
ORDER BY recovery_time, patient_name 
;