-- SELECT name
-- FROM Customer
-- WHERE referee_id <> 2
-- OR referee_id IS NULL;

SELECT name
FROM (SELECT name,
CASE
    WHEN referee_id = 2 THEN TRUE
    ELSE FALSE
END AS referee
FROM Customer) ref
WHERE referee IS FALSE;