SELECT a.name AS Customers
FROM Customers a
LEFT JOIN Orders b
ON a.id = b.customerId
WHERE b.id IS NULL;

-- solution
-- select customers.name as 'Customers'
-- from customers
-- where customers.id not in
-- (
--     select customerid from orders
-- );