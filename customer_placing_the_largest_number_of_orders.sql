SELECT customer_number
FROM
(SELECT customer_number, COUNT(customer_number) AS order_count
FROM Orders
GROUP BY customer_number
ORDER BY order_count DESC LIMIT 1) a;

-- no subquery
SELECT
    customer_number
FROM
    orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1
;

-- subquery + having
SELECT customer_number
FROM orders
GROUP BY customer_number
HAVING COUNT(order_number) = (
	SELECT COUNT(order_number) cnt
	FROM orders
	GROUP BY customer_number
	ORDER BY cnt DESC
	LIMIT 1
)

-- rank -> much slower
select customer_number
from (
select customer_number, rank() over (order by count(1) desc) rank_val
from orders
group by customer_number
) a where rank_val = 1