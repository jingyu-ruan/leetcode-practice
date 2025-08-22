# Write your MySQL query statement below
(
SELECT u.name AS results
FROM Users u
JOIN MovieRating mr ON u.user_id = mr.user_id
GROUP BY mr.user_id
ORDER BY COUNT(*) DESC, u.name ASC
LIMIT 1
)

UNION ALL
(
SELECT m.title
FROM MovieRating mr
JOIN Movies m ON m.movie_id = mr.movie_id 
WHERE LEFT(created_at, 7) = '2020-02'
GROUP BY mr.movie_id    
ORDER BY AVG(rating) DESC, m.title ASC
LIMIT 1
);
