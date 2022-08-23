SELECT name, SUM(amount) AS balance
FROM Users u
LEFT JOIN Transactions t ON u.account = t.account
GROUP BY name
HAVING balance > 10000;