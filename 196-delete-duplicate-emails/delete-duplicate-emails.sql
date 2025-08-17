# Write your MySQL query statement below
DELETE p1 
FROM Person p1
JOIN Person p2
    USING(email)
    WHERE p1.id > p2.id;









