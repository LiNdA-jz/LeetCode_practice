-- does not work
SELECT buyer_id, join_date, IFNULL(COUNT(order_date),0) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o ON u.user_id = o.buyer_id
WHERE YEAR(order_date) = '2019'
GROUP BY buyer_id;

-- join on two conditions
SELECT u.user_id AS buyer_id, join_date, COUNT(order_date) AS orders_in_2019 
FROM Users as u
LEFT JOIN Orders as o
ON u.user_id = o.buyer_id
AND YEAR(order_date) = '2019'
GROUP BY u.user_id