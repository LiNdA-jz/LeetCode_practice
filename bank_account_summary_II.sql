SELECT name, SUM(amount) AS balance
FROM Users u
LEFT JOIN Transactions t ON u.account = t.account
GROUP BY u.account
HAVING balance > 10000;

-- Common Table Expression
-- "A common table expression (CTE) is a named temporary result set 
-- that exists within the scope of a single statement and that can be referred to later within that statement,
-- possibly multiple times."
with tmp as(
select t.account, u.name, sum(amount) as balance
from Transactions t
left join Users u on t.account = u.account
group by account )

select name, balance
from tmp
where balance > 10000

-- using
select name, sum(amount) balance
from users
left join transactions
using(account)
group by account
having balance > 10000