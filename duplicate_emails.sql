SELECT email AS Email
FROM
(SELECT email, COUNT(*)
FROM Person
GROUP BY email
HAVING COUNT(*)>1) a;