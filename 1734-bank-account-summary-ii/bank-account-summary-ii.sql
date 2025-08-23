# Write your MySQL query statement below

SELECT u.name, SUM(amount) AS  balance -- ?
FROM Transactions t
LEFT JOIN Users u ON u.account = t.account
GROUP BY t.account
HAVING balance > 10000;
