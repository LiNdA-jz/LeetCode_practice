SELECT email AS Email
FROM
(SELECT email, COUNT(*)
FROM Person
GROUP BY email
HAVING COUNT(*)>1) a;

-- without subquery
select Email
from Person
group by Email
having count(Email) > 1;

-- where
select Email from
(
  select Email, count(Email) as num
  from Person
  group by Email
) as statistic
where num > 1
;

-- inner join
SELECT distinct p1.Email from Person p1
INNER JOIN Person p2
ON p1.Email = p2.Email AND p1.Id <> p2.Id;