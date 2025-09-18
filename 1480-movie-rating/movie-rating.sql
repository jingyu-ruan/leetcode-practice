WITH merged AS (
    SELECT mr.movie_id, mr.user_id, rating, created_at, title, name
    FROM MovieRating mr
    LEFT JOIN Movies m ON mr.movie_id = m.movie_id
    LEFT JOIN Users u ON u.user_id = mr.user_id
), max_name AS (
    SELECT name, COUNT(name) AS cnt
    FROM merged
    GROUP BY user_id
    ORDER BY cnt DESC, name ASC
    LIMIT 1
), max_rate AS (
    SELECT title, AVG(rating) AS avg_r
    FROM merged
    WHERE LEFT(created_at, 7) = '2020-02'
    GROUP BY movie_id
    ORDER BY avg_r DESC, title
    LIMIT 1
)

SELECT name AS results  
FROM max_name
UNION ALL
SELECT title
FROM max_rate
;