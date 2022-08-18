SELECT a.firstName, ablastName, b.city, b.state
FROM Person a
LEFT JOIN Address b
ON a.personId = b.personId;