WITH m AS (
    SELECT player_id, 
           MIN(event_date) OVER (PARTITION BY player_id ) AS min_date, 
           event_date 
    FROM Activity 
), fst_login AS (
    SELECT player_id, min_date, event_date
    FROM m
    WHERE DATEDIFF(event_date, min_date) = 1
)
SELECT ROUND(COUNT(*) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction  
FROM fst_login
;
