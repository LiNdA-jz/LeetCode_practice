SELECT DISTINCT customer_id, COUNT(v.visit_id) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE v.visit_id NOT IN
(SELECT visit_id
FROM Transactions)
GROUP BY customer_id
ORDER BY count_no_trans DESC;

-- not null
SELECT
	customer_id,
	COUNT(Visits.visit_id) AS count_no_trans
FROM
	visits
LEFT JOIN Transactions
	ON Visits.visit_id = Transactions.visit_id
WHERE 
	Transactions.visit_id IS NULL
GROUP BY customer_id

-- natural join
SELECT customer_id, COUNT(v.visit_id) AS count_no_trans 
FROM Visits v
NATURAL LEFT JOIN Transactions t
WHERE t.visit_id IS NULL
GROUP BY customer_id

-- faster
-- BUT In the above solution, notice that we are using NOT IN. In order for this to work, the subquery will be executed first and it will return a list of all distinct visit_id from Transactions. After that, the outer query is executed for each visit_id in Visits table and compared against this list returned from the inner query.
-- This is why a join is better than a subquery in this case.
SELECT customer_id, COUNT(*) as count_no_trans
FROM Visits
WHERE visit_id NOT IN (SELECT DISTINCT visit_id FROM Transactions)
GROUP BY customer_id;