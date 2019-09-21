WITH to_gbp_rates AS (
    SELECT
        DISTINCT ON (from_currency, to_currency) from_currency, to_currency,
        last_value(rate) OVER (
            PARTITION BY from_currency, to_currency
            ORDER BY ts ASC
            ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
        ) AS rate
    FROM exchange_rates
    WHERE to_currency = 'GBP'
    ORDER BY from_currency
)
SELECT
    user_id,
    sum(converted) AS total_spent_gbp
FROM (
    SELECT
        DISTINCT user_id,
        CASE
            WHEN currency = 'GBP' THEN amount
            ELSE amount * rate
        END AS converted
    FROM transactions txn
    JOIN to_gbp_rates ON
        txn.currency = to_gbp_rates.from_currency
        OR txn.currency = 'GBP'
) converted_txns
GROUP BY user_id
ORDER BY user_id;
