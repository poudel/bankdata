WITH txns AS (
    SELECT
        user_id,
        txn.ts as txn_ts,
        er.ts AS er_ts,
        amount, rate, txn.currency AS txn_currency
    FROM transactions txn LEFT JOIN exchange_rates er
    ON txn.currency = er.from_currency
        AND er.ts <= txn.ts
	    AND er.to_currency = 'GBP'
)
SELECT
    user_id,
    sum(COALESCE(amount * latest_rate, amount))  AS total_spent_gbp
FROM (
    SELECT
        DISTINCT ON (user_id, txn_ts, txn_currency, amount) user_id, txn_ts, txn_currency, amount,
        last_value(rate) OVER (
            PARTITION BY user_id, txn_ts, txn_currency, amount
            ORDER BY er_ts ASC
            ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
        ) AS latest_rate
    FROM txns
) txns_distinct
GROUP BY user_id
ORDER BY user_id;
