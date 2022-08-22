SELECT customer_number
FROM
(SELECT customer_number, COUNT(customer_number) AS order_count
FROM Orders
GROUP BY customer_number
ORDER BY order_count DESC LIMIT 1) a;