SELECT user_id, CONCAT(UPPER(LEFT(name,1)), LOWER(SUBSTR(name, 2, LENGTH(name)))) AS name
FROM Users
ORDER BY user_id;

-- faster
SELECT user_id, CONCAT(UPPER(LEFT(name,1)), LOWER(SUBSTRING(name,2))) as name
FROM Users
ORDER BY user_id;