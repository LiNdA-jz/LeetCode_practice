-- not work
SELECT p.product_id, product_name
FROM Product p
INNER JOIN Sales s ON p.product_id = s.product_id  AND s.sale_date >= '2019-01-01' AND s.sale_date <= '2019-03-31';

-- use MIN and MAX
SELECT s.product_id, product_name
FROM Sales s
LEFT JOIN Product p
ON s.product_id = p.product_id
GROUP BY s.product_id
HAVING MIN(sale_date) >= CAST('2019-01-01' AS DATE) AND
       MAX(sale_date) <= CAST('2019-03-31' AS DATE)

-- subquery
SELECT product_id, product_name 
FROM Product 
WHERE product_id IN
(SELECT product_id
FROM Sales
GROUP BY product_id
HAVING MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31')