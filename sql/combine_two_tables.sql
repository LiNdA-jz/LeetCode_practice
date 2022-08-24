SELECT a.firstName, ablastName, b.city, b.state
FROM Person a
LEFT JOIN Address b
ON a.personId = b.personId;

-- using
SELECT FirstName, LastName, City, State
FROM Person LEFT JOIN Address USING (PersonId)