SELECT s.name
FROM SalesPerson AS s
WHERE NOT EXISTS (
  SELECT 1
  FROM Orders AS o
  JOIN Company AS c ON c.com_id = o.com_id
  WHERE o.sales_id = s.sales_id
    AND c.name = 'RED'
);
