# Budgeting Analysis Project

## Overview
This project demonstrates an end-to-end budgeting and financial analysis workflow using real-world style bank transaction data. It includes:
- Data cleaning (Python)
- Categorization logic (e.g., “Incoming Transfer,” “Bank Charges,” etc.)
- Database integration (PostgreSQL via SQLAlchemy)
- Data visualization (Tableau dashboards)

## Folder Structure

Budgeting Analysis/ 

├── data/ │

    ├── bank.csv # Raw data │ 
    ├── cleaned_bank.csv │
├── notebooks/ │ 

    ├── 01_data_cleaning.ipynb │ 
    └── 02_eda_and_visuals.ipynb 
├── scripts/ │ 

    ├── clean_data_and_load.py │ 
    └── categorize_transactions.py 
├── Dashboard.twbx

├──sql│ 

    ├──queries
├── venv/ 

├── README.md 

├── .gitignore  

└── requirements.txt

## Features
1. **Data Cleaning & Transformation**: Standardizes columns, handles missing values, converts data types.
2. **Categorization**: Automatically categorizes transactions based on keywords (e.g., "TRF FROM" → "Incoming Transfer").
3. **PostgreSQL Integration**: Inserts cleaned data into a `transactions` table using SQLAlchemy.
4. **Tableau Dashboards**: Showcases:
   - Bar Chart by Category
   - Monthly Deposits vs. Withdrawals
   - Cumulative Balance Over Time
   - Net Monthly Cash Flow

## Data Source
- **Bank CSV**: Derived from a public Kaggle dataset or your own anonymized data.
- [Kaggle: Bank Marketing Campaign](https://www.kaggle.com/code/mammadabbasli/bank-marketing-campaign) (Reference)

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/YourUsername/BudgetingAnalysis.git
cd BudgetingAnalysis
```
### 2. Create & Activate a Virtual Environment (Optional)
```bash
python -m venv venv
# For Windows PowerShell:
.\venv\Scripts\Activate.ps1
# For Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Data Cleaning & Loading Script

Update clean_data_and_load.py with your PostgreSQL credentials.

Run the script:

```bash
python clean_data_and_load.py
```
This cleans bank.csv and loads the data into a transactions table in your PostgreSQL database.

### 5. Explore the Data & Visualizations
Python Notebooks: In notebooks/, see the data cleaning and exploratory analysis.

Tableau Dashboard: Open in the web [here](https://public.tableau.com/views/DashboardBudgetingProject/MarketingCampaignFinancialDashboard20152019?:language=es-ES&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

### 6. Usage:

Personal Budgeting: Replace bank.csv with your own statement (ensure consistent column naming).

Portfolio Demonstration: Use the included sample data to show your financial analysis process.

### 7. Requirements:

Python 3.8+

PostgreSQL (for database loading)

Tableau (for dashboard viewing)

## 8. Contribution & Contact

This project is a key component of my **Financial Data Science Portfolio**. It demonstrates my expertise in quantitative analysis, data cleaning, data transformation, and data visualization through an end-to-end budgeting analysis workflow using real-world bank transaction data.


For any questions or to discuss potential collaborations, please feel free to reach out via:


**Name:** Erick Guagua

**Email:** erick.guagua@yachaytech.edu.ec

**Contact:** [Linkedin](https://www.linkedin.com/in/erick-guagua-14b143214/)
