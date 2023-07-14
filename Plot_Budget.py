import budgeting_lib as bl
import budgeting_other_lib as bol
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

dates = [
        (dt.date(2023, 7, 11), dt.date(2024, 3, 14)),
        (dt.date(2024, 3, 15), dt.date(2025, 3, 14)),
        (dt.date(2025, 3, 15), dt.date(2025, 12, 31))
        ]

# name, amount, category, frequency, duedate, and ifweekday
bills = [
    [
        {'name': 'SameYou', 'amount': 5.15, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 1, 'ifweekday': True},
        {'name': 'Disney+', 'amount': 10.99, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 2, 'ifweekday': False},
        {'name': 'Spotify', 'amount': 9.99, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 14, 'ifweekday': False},
        {'name': 'Phone Bill', 'amount': 50, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 20, 'ifweekday': False},
        {'name': 'Other Insure', 'amount': 100, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 22, 'ifweekday': False},
        {'name': 'Internet', 'amount': 69.95, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 30, 'ifweekday': False},
        {'name': 'Rent', 'amount': 1000, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 1, 'ifweekday': False},
        {'name': 'Utilities', 'amount': 120, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 1, 'ifweekday': False},
        {'name': 'Health Insurance', 'amount': 116, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 1, 'ifweekday': False},
        {'name': 'CoPilot', 'amount': 10, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 2, 'ifweekday': False}
    ],
    [
        {'name': 'SameYou', 'amount': 5.15, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 1, 'ifweekday': True},
        {'name': 'Disney+', 'amount': 10.99, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 2, 'ifweekday': False},
        {'name': 'Spotify', 'amount': 9.99, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 14, 'ifweekday': False},
        {'name': 'Phone Bill', 'amount': 50, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 20, 'ifweekday': False},
        {'name': 'Other Insure', 'amount': 100, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 22, 'ifweekday': False},
        {'name': 'Internet', 'amount': 69.95, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 30, 'ifweekday': False},
        {'name': 'Rent', 'amount': 1000, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 1, 'ifweekday': False},
        {'name': 'Utilities', 'amount': 120, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 1, 'ifweekday': False},
        {'name': 'Health Insurance', 'amount': 116, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 1, 'ifweekday': False},
        {'name': 'CoPilot', 'amount': 10, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 2, 'ifweekday': False}
    ],
    [
        {'name': 'SameYou', 'amount': 5.15, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 1, 'ifweekday': True},
        {'name': 'Disney+', 'amount': 10.99, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 2, 'ifweekday': False},
        {'name': 'Spotify', 'amount': 9.99, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 14, 'ifweekday': False},
        {'name': 'Phone Bill', 'amount': 50, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 20, 'ifweekday': False},
        {'name': 'Other Insure', 'amount': 100, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 22, 'ifweekday': False},
        {'name': 'Internet', 'amount': 69.95, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 30, 'ifweekday': False},
        {'name': 'Rent', 'amount': 1000, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 1, 'ifweekday': False},
        {'name': 'Utilities', 'amount': 120, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 1, 'ifweekday': False},
        {'name': 'Health Insurance', 'amount': 116, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 1, 'ifweekday': False},
        {'name': 'CoPilot', 'amount': 10, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 2, 'ifweekday': False}
    ],
    ]

# name, amount, category, description
expenses = [
    [
        {'name': 'Gas', 'amount': 100, 'category': 'Expense', 'description': 'Gas for the car'},
        {'name': 'Groceries', 'amount': 350, 'category': 'Expense', 'description': 'Groceries for the month'},
    ],
    [
        {'name': 'Gas', 'amount': 100, 'category': 'Expense', 'description': 'Gas for the car'},
        {'name': 'Groceries', 'amount': 350, 'category': 'Expense', 'description': 'Groceries for the month'},
    ],
    [
        {'name': 'Gas', 'amount': 100, 'category': 'Expense', 'description': 'Gas for the car'},
        {'name': 'Groceries', 'amount': 350, 'category': 'Expense', 'description': 'Groceries for the month'},
    ],
    ]

# name, amount, payday, ifweekday, category, frequency
incomes = [
    [
        {'name': 'Paycheck', 'amount': 1500, 'payday': 14, 'ifweekday': True, 'category': 'Income', 'frequency': 'Biweekly'},
    ],
    [
        {'name': 'Paycheck', 'amount': 1600, 'payday': 14, 'ifweekday': True, 'category': 'Income', 'frequency': 'Biweekly'},
    ],
    [
        {'name': 'Paycheck', 'amount': 1700, 'payday': 14, 'ifweekday': True, 'category': 'Income', 'frequency': 'Biweekly'},
    ],
    ]

# name, type
accounts = [
    [
        {'name': 'Checking', 'type': 'checking'},
        {'name': 'Savings', 'type': 'savings'},
        {'name': 'Travel', 'type': 'savings'},
        {'name': 'Student Loan', 'type': 'loan'},
    ],
    [
        {'name': 'Checking', 'type': 'checking'},
        {'name': 'Savings', 'type': 'savings'},
        {'name': 'Travel', 'type': 'savings'},
        {'name': 'Student Loan', 'type': 'loan'},
    ],
    [
        {'name': 'Checking', 'type': 'checking'},
        {'name': 'Savings', 'type': 'savings'},
        {'name': 'Travel', 'type': 'savings'},
        {'name': 'Student Loan', 'type': 'loan'},
    ]
    ]

# name, amount, from_account, to_account, frequency, depositday
transfers = [
    [
        {'name': 'Checking to Savings', 'amount': 300, 'from_account': 'Checking', 'to_account': 'Savings', 'frequency': 'biweekly', 'depositday': 14},
        {'name': 'Checking to Travel', 'amount': 50, 'from_account': 'Checking', 'to_account': 'Travel', 'frequency': 'biweekly', 'depositday': 14},
        {'name': 'Checking to Student Loan', 'amount': 500, 'from_account': 'Checking', 'to_account': 'Student Loan', 'frequency': 'monthly', 'depositday': 14},
    ],
    [
        {'name': 'Checking to Savings', 'amount': 400, 'from_account': 'Checking', 'to_account': 'Savings', 'frequency': 'biweekly', 'depositday': 14},
        {'name': 'Checking to Travel', 'amount': 50, 'from_account': 'Checking', 'to_account': 'Travel', 'frequency': 'biweekly', 'depositday': 14},
        {'name': 'Checking to Student Loan', 'amount': 500, 'from_account': 'Checking', 'to_account': 'Student Loan', 'frequency': 'monthly', 'depositday': 14},
    ],
    [
        {'name': 'Checking to Savings', 'amount': 500, 'from_account': 'Checking', 'to_account': 'Savings', 'frequency': 'biweekly', 'depositday': 14},
        {'name': 'Checking to Travel', 'amount': 50, 'from_account': 'Checking', 'to_account': 'Travel', 'frequency': 'biweekly', 'depositday': 14},
        {'name': 'Checking to Student Loan', 'amount': 500, 'from_account': 'Checking', 'to_account': 'Student Loan', 'frequency': 'monthly', 'depositday': 14},
    ],
    ]

# name
budgets = [
    {'name': 'budget1'},
    {'name': 'budget2'},
    {'name': 'budget3'}
    ]
initial_balances = [334,2015,664.26,0,0]

summary = bol.summary_dataframe(dates, bills, expenses, incomes, accounts, transfers, budgets, initial_balances)

# Drop the total spent, total income, and total balance columns
summary = summary.drop(columns=['Total Spent', 'Total Earned', 'Total Balance'])

# Plot the dataframe
summary.plot(figsize=(20,15))
plt.axhline(y=0, color='black', linestyle='--')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Balance', fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title(f'Budget Plot', fontsize=20)
plt.legend(loc='upper left', fontsize=18)

# Show the final balance for each account on the plot as a label
for account in summary.columns:
    plt.text(summary.index[-1], summary[account].iloc[-1], str(int(summary[account].iloc[-1])), fontsize=12)

plt.tight_layout()

# Save the plot
plt.savefig('plot_budget.png')