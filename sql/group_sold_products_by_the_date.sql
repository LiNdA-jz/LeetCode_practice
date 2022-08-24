-- GROUP_CONCAT
-- SELECT col1, col2, ..., colN
-- GROUP_CONCAT ( [DISTINCT] col_name1 
-- [ORDER BY clause]  [SEPARATOR str_val] ) 
-- FROM table_name GROUP BY col_name2;
SELECT sell_date,
COUNT(*) AS num_sold,
GROUP_CONCAT(product ORDER BY product) AS products
FROM (SELECT DISTINCT sell_date,product
FROM Activities) AS act
GROUP BY sell_date
ORDER BY sell_date;

-- slower without nested SELECT
-- select distinct sell_date,
-- count(distinct product) as num_sold,
-- group_concat(distinct product order by product) as products
-- from Activities
-- group by sell_date
-- order by sell_date;