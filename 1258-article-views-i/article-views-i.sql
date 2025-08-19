# Write your MySQL query statement below

SELECT DISTINCT author_id AS id
FROM Views 
WHERE author_id - viewer_id =0
ORDER BY author_id
