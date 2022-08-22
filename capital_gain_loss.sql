-- subquery worked
-- cannot use price=case..., otherwise, it is a boolean type
SELECT stock_name, SUM(price_signed) AS capital_gain_loss
FROM
(SELECT stock_name, operation_day,
CASE
    WHEN operation = 'Sell' THEN price
    ELSE -1*price
    END AS price_signed
FROM Stocks
GROUP BY stock_name, operation_day) a
GROUP BY stock_name;

-- no subquery
SELECT stock_name, SUM(
    CASE
        WHEN operation = 'Buy' THEN -price
        ELSE price
    END
) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name

-- if
select stock_name
, sum(if(operation = 'Buy', -1, 1) * price) as capital_gain_loss
from stocks
group by stock_name