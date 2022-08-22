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