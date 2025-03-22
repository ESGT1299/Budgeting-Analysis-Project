-- Query: Total Deposits by Month
SELECT DATE_TRUNC('month', date) AS month, SUM(deposit_amt) AS total_deposit
FROM transactions
GROUP BY month
ORDER BY month;

-- Query: Withdrawals by Category
SELECT category, SUM(withdrawal_amt) AS total_withdrawal, COUNT(*) AS transaction_count
FROM transactions
GROUP BY category;





