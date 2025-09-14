SELECT DISTINCT s.product_id, p.product_name
FROM Sales s
LEFT JOIN Product p on p.product_id =s.product_id 
WHERE sale_date BETWEEN '2019-01-01' AND '2019-03-31'
AND s.product_id NOT IN (SELECT product_id FROM Sales WHERE sale_date >= '2019-04-01' OR sale_date < '2019-01-01')
;
