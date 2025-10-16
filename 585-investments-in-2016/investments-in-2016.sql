WITH m AS (
    SELECT tiv_2016, 
        COUNT(tiv_2015) OVER (PARTITION BY tiv_2015) AS cnt_2015, 
        COUNT(CONCAT(lat, lon)) OVER (PARTITION BY lat, lon) AS cnt_pos
    FROM Insurance 
)
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016 
FROM m
WHERE cnt_2015 > 1 AND cnt_pos = 1
;