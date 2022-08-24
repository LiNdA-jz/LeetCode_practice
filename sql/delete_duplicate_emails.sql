DELETE t1
FROM Person t1
INNER JOIN Person t2
ON t1.id > t2.id
AND t1.email = t2.email;

-- JOIN & WHERE
DELETE p2
FROM Person p1
JOIN Person p2
ON p1.Email = p2.Email
WHERE p1.id< p2.id;

-- "official"
DELETE p1 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id

-- with select -> faster
DELETE FROM Person WHERE Id NOT IN 
(SELECT * FROM(
    SELECT MIN(Id) FROM Person GROUP BY Email) as p);