import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
df = pd.read_csv("data/cleaned_bank.csv", parse_dates=['date'])

# Plot: Transaction Count by Category
plt.figure(figsize=(10,6))
sns.countplot(data=df, x='category', order=df['category'].value_counts().index)
plt.title("Transaction Count by Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot: Monthly Deposits and Withdrawals
df['month'] = df['date'].dt.to_period('M')
monthly = df.groupby('month')[['deposit_amt', 'withdrawal_amt']].sum().reset_index()
monthly['month'] = monthly['month'].astype(str)

plt.figure(figsize=(10,6))
plt.plot(monthly['month'], monthly['deposit_amt'], marker='o', label='Deposit')
plt.plot(monthly['month'], monthly['withdrawal_amt'], marker='o', label='Withdrawal')
plt.title("Monthly Deposits and Withdrawals")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
