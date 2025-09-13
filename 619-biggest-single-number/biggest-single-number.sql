WITH unq AS 
(SELECT num, COUNT(num) OVER ( PARTITION BY num) AS cnt
FROM MyNumbers)
SELECT MAX(num) AS num
FROM unq
WHERE cnt =1 
;

