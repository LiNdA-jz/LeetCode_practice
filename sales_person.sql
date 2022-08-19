SELECT s.name
FROM SalesPerson s
WHERE s.sales_id NOT IN (SELECT o.sales_id
FROM Orders o
JOIN Company c
ON o.com_id = c.com_id
WHERE c.name = "RED");

-- official
SELECT
    s.name
FROM
    salesperson s
WHERE
    s.sales_id NOT IN (SELECT
            o.sales_id
        FROM
            orders o
                LEFT JOIN
            company c ON o.com_id = c.com_id
        WHERE
            c.name = 'RED')
;

-- right join without subquery -> faster
select salesperson.name
from orders o join company c on (o.com_id = c.com_id and c.name = 'RED')
right join salesperson on salesperson.sales_id = o.sales_id
where o.sales_id is null