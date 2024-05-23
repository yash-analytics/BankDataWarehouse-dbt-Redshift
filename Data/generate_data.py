import pandas as pd
from datetime import datetime, timedelta
import random

def generate_dim_accounts():
    data = {
        'account_id': range(1, 101),
        'customer_id': range(1, 101),
        'account_number': [f"1000{i}" for i in range(1, 101)],
        'account_type': ['Checking', 'Savings'] * 50,
        'account_balance': [round(1000.00 * i, 2) for i in range(1, 101)],
        'credit_score': [random.randint(600, 800) for _ in range(100)],
        'created_at': [datetime.now() - timedelta(days=random.randint(1, 365)) for _ in range(100)]
    }
    df = pd.DataFrame(data)
    df.to_csv('dim_accounts.csv', index=False)

def generate_dim_channels():
    data = {
        'channel_id': range(1, 11),
        'channel_name': ['Online', 'Phone', 'Branch', 'ATM', 'Mobile', 'Social Media', 'Email', 'Fax', 'Mail', 'Field Visit'],
        'created_at': [datetime.now() - timedelta(days=random.randint(1, 365)) for _ in range(10)]
    }
    df = pd.DataFrame(data)
    df.to_csv('dim_channels.csv', index=False)

def generate_dim_currencies():
    data = {
        'currency_id': range(1, 21),
        'currency_code': ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD'] * 2,
        'currency_name': ['US Dollar', 'Euro', 'Japanese Yen', 'Pound Sterling', 'Australian Dollar', 'Canadian Dollar', 'Swiss Franc', 'Chinese Yuan', 'Swedish Krona', 'New Zealand Dollar'] * 2,
        'created_at': [datetime.now() - timedelta(days=random.randint(1, 365)) for _ in range(20)]
    }
    df = pd.DataFrame(data)
    df.to_csv('dim_currencies.csv', index=False)

def generate_dim_customers():
    data = {
        'customer_id': range(1, 101),
        'first_name': [f"First{i}" for i in range(1, 101)],
        'last_name': [f"Last{i}" for i in range(1, 101)],
        'full_name': [f"First{i} Last{i}" for i in range(1, 101)],
        'email': [f"email{i}@example.com" for i in range(1, 101)],
        'address': [f"{i} Main St" for i in range(1, 101)],
        'city': ['City' + str(i%10) for i in range(1, 101)],
        'state': ['State' + str(i%10) for i in range(1, 101)],
        'postal_code': [f"{10000 + i}" for i in range(1, 101)],
        'phone_number': [f"555-0100{i}" for i in range(1, 101)],
        'created_at': [datetime.now() - timedelta(days=random.randint(1, 365)) for i in range(1, 101)]
    }
    df = pd.DataFrame(data)
    df.to_csv('dim_customers.csv', index=False)

def generate_dim_dates():
    date_range = pd.date_range(start='2022-01-01', end='2023-01-01', freq='D')
    data = {
        'date_id': range(1, len(date_range)+1),
        'date': [date.strftime('%Y-%m-%d') for date in date_range],
        'day': [date.day for date in date_range],
        'month': [date.month for date in date_range],
        'year': [date.year for date in date_range],
        'weekday': [date.strftime('%A') for date in date_range],
        'created_at': [datetime.now() - timedelta(days=random.randint(1, 365)) for _ in date_range]
    }
    df = pd.DataFrame(data)
    df.to_csv('dim_dates.csv', index=False)

def generate_dim_investment_types():
    types = ['Stocks', 'Bonds', 'Real Estate', 'Commodities', 'Mutual Funds', 'ETFs', 'Crypto']
    data = {
        'investment_type_id': range(1, 8),
        'investment_type_name': types,
        'created_at': [datetime.now() - timedelta(days=random.randint(1, 365)) for _ in types]
    }
    df = pd.DataFrame(data)
    df.to_csv('dim_investment_types.csv', index=False)

def generate_dim_loans():
    data = {
        'loan_id': range(1, 101),
        'loan_type': ['Personal', 'Mortgage', 'Auto', 'Student'] * 25,
        'loan_amount': [random.randint(5000, 50000) for _ in range(100)],
        'interest_rate': [round(random.uniform(1.5, 8.5), 2) for _ in range(100)],
        'created_at': [datetime.now() - timedelta(days=random.randint(1, 365)) for _ in range(100)]
    }
    df = pd.DataFrame(data)
    df.to_csv('dim_loans.csv', index=False)

def generate_dim_locations():
    data = {
        'location_id': range(1, 51),
        'city': ['City' + str(i%10) for i in range(1, 51)],
        'state': ['State' + str(i%10) for i in range(1, 51)],
        'country': ['Country' + str(i%5) for i in range(1, 51)],
        'postal_code': [f"{90000 + i}" for i in range(1, 51)],
        'created_at': [datetime.now() - timedelta(days=random.randint(1, 365)) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('dim_locations.csv', index=False)

def generate_dim_transaction_types():
    types = ['Deposit', 'Withdrawal', 'Transfer', 'Payment']
    data = {
        'transaction_type_id': range(1, 5),
        'transaction_type_name': types,
        'created_at': [datetime.now() - timedelta(days=random.randint(1, 365)) for _ in types]
    }
    df = pd.DataFrame(data)
    df.to_csv('dim_transaction_types.csv', index=False)

def generate_fact_customer_interactions():
    data = {
        'interaction_id': range(1, 201),
        'date_id': [random.randint(1, 365) for _ in range(200)],
        'channel_id': [random.randint(1, 10) for _ in range(200)],
        'location_id': [random.randint(1, 50) for _ in range(200)],
        'customer_id': [random.randint(1, 100) for _ in range(200)],
        'interaction_type': ['Inquiry', 'Complaint', 'Feedback', 'Support'] * 50,
        'interaction_rating': [random.randint(1, 5) for _ in range(200)],
        'created_at': [datetime.now() - timedelta(days=random.randint(1, 365)) for _ in range(200)]
    }
    df = pd.DataFrame(data)
    df.to_csv('fact_customer_interactions.csv', index=False)

def generate_fact_daily_balances():
    data = {
        'balance_id': range(1, 301),
        'date_id': [random.randint(1, 365) for _ in range(300)],
        'account_id': [random.randint(1, 100) for _ in range(300)],
        'currency_id': [random.randint(1, 20) for _ in range(300)],
        'opening_balance': [round(1000 * random.random(), 2) for _ in range(300)],
        'closing_balance': [round(1000 * random.random(), 2) for _ in range(300)],
        'average_balance': [round(1000 * random.random(), 2) for _ in range(300)],
        'created_at': [datetime.now() - timedelta(days=random.randint(1, 365)) for _ in range(300)]
    }
    df = pd.DataFrame(data)
    df.to_csv('fact_daily_balances.csv', index=False)

def generate_fact_investments():
    data = {
        'investment_id': range(1, 201),
        'date_id': [random.randint(1, 365) for _ in range(200)],
        'account_id': [random.randint(1, 100) for _ in range(200)],
        'investment_type_id': [random.randint(1, 7) for _ in range(200)],
        'amount_invested': [round(5000 * random.random(), 2) for _ in range(200)],
        'return': [round(100 * random.random(), 2) for _ in range(200)],
        'created_at': [datetime.now() - timedelta(days=random.randint(1, 365)) for _ in range(200)]
    }
    df = pd.DataFrame(data)
    df.to_csv('fact_investments.csv', index=False)

def generate_fact_loans():
    data = {
        'loan_id': range(1, 151),
        'date_id': [random.randint(1, 365) for _ in range(150)],
        'customer_id': [random.randint(1, 100) for _ in range(150)],
        'loan_type_id': [random.randint(1, 4) for _ in range(150)],
        'loan_amount': [round(10000 * random.random(), 2) for _ in range(150)],
        'interest_rate': [round(5 + 10 * random.random(), 2) for _ in range(150)],
        'created_at': [datetime.now() - timedelta(days=random.randint(1, 365)) for _ in range(150)]
    }
    df = pd.DataFrame(data)
    df.to_csv('fact_loans.csv', index=False)

def generate_fact_transactions():
    data = {
        'transaction_id': range(1, 501),
        'date_id': [i % 365 + 1 for i in range(1, 501)],
        'account_id': [i % 100 + 1 for i in range(1, 501)],
        'transaction_type_id': [i % 4 + 1 for i in range(1, 501)],
        'amount': [round(100.0 * random.random(), 2) for i in range(1, 501)],
        'created_at': [datetime.now() - timedelta(days=i % 30) for i in range(1, 501)]
    }
    df = pd.DataFrame(data)
    df.to_csv('fact_transactions.csv', index=False)

# Call all generation functions
generate_dim_accounts()
generate_dim_channels()
generate_dim_currencies()
generate_dim_customers()
generate_dim_dates()
generate_dim_investment_types()
generate_dim_loans()
generate_dim_locations()
generate_dim_transaction_types()

generate_fact_customer_interactions()
generate_fact_daily_balances()
generate_fact_investments()
generate_fact_loans()
generate_fact_transactions()

print("Data generation for all tables complete. CSV files saved locally.")