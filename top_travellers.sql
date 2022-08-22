-- order by using "," to separate
-- need group by id
SELECT u.name, SUM(IF(r.distance IS NULL, 0, r.distance)) AS travelled_distance
FROM Users u
LEFT JOIN Rides r ON u.id = r.user_id
GROUP BY u.id
ORDER BY travelled_distance DESC, u.name;

-- ifnull
select u.name, ifnull(sum(r.distance), 0) as travelled_distance
from users u
left join rides r
on u.id = r.user_id
group by r.user_id
order by travelled_distance desc, u.name asc

-- partition by
SELECT DISTINCT u.name, 
IFNULL(SUM(distance) OVER (PARTITION BY user_id), 0) as travelled_distance 
FROM Rides r RIGHT JOIN Users u ON r.user_id = u.id 
ORDER BY travelled_distance DESC, name

-- coalesce
-- use the SQL COALESCE() function to replace the NULL value with a simple text
select u.name, coalesce(sum(r.distance),0) as "travelled_distance"
from users as u
left join rides as r
on u.id = r.user_id
group by u.name
order by travelled_distance desc, u.name