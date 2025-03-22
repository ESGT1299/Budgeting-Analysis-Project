import pandas as pd
from sqlalchemy import create_engine

# --- Configuration ---
db_username = "postgres"
db_password = "ESgt09601698."  # Replace with your password
db_host = "localhost"
db_port = "5432"
db_name = "budgeting_db"

# Create SQLAlchemy Engine
engine = create_engine(f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}")

# --- Data Ingestion ---
df = pd.read_csv("data/bank.csv")
print("Original Columns:", df.columns)

# --- Data Cleaning ---
# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Retain necessary columns
df = df[['date', 'transaction_details', 'withdrawal_amt', 'deposit_amt', 'balance_amt']]

# Convert date to datetime and clean numeric columns (remove commas, convert to float)
df['date'] = pd.to_datetime(df['date'], errors='coerce')
for col in ['withdrawal_amt', 'deposit_amt', 'balance_amt']:
    df[col] = df[col].astype(str).str.replace(',', '').astype(float).fillna(0)

# --- Enhanced Categorization ---
def categorize_transaction(detail, withdrawal, deposit):
    """
    Categorize transactions based on details and amount.
    
    Rules (refined via EDA):
    - If details indicate incoming transfers ("trf from" or "trf frm"), label as "Incoming Transfer".
    - If details suggest internal movements ("internal fund" or "fdrl"), label as "Internal Fund Transfer".
    - If details mention "remi", consider it a "Remittance Fee".
    - If details mention "gibl", label it as "Bank Charges".
    - Otherwise, use amount information:
         * deposit > 0 and withdrawal == 0 → "Deposit"
         * withdrawal > 0 and deposit == 0 → "Withdrawal"
         * Else → "Other"
    """
    detail_lower = str(detail).lower()
    
    if "trf from" in detail_lower or "trf frm" in detail_lower:
        return "Incoming Transfer"
    elif "internal fund" in detail_lower or "fdrl" in detail_lower:
        return "Internal Fund Transfer"
    elif "remi" in detail_lower:
        return "Remittance Fee"
    elif "gibl" in detail_lower:
        return "Bank Charges"
    else:
        if deposit > 0 and withdrawal == 0:
            return "Deposit"
        elif withdrawal > 0 and deposit == 0:
            return "Withdrawal"
        else:
            return "Other"

# Apply categorization row by row
df['category'] = df.apply(lambda row: categorize_transaction(row['transaction_details'],
                                                               row['withdrawal_amt'],
                                                               row['deposit_amt']),
                          axis=1)

print("Sample Data After Categorization:")
print(df.head(15))

# --- Save Cleaned Data ---
df.to_csv("data/cleaned_bank.csv", index=False)
print("✅ Cleaned data saved to 'data/cleaned_bank.csv'")

# --- Insert Cleaned Data into PostgreSQL (Replace Table) ---
df.to_sql('transactions', engine, if_exists='replace', index=False)
print("✅ Data successfully inserted into PostgreSQL (table replaced)!")



