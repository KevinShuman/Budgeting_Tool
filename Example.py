# This is a test example that determines the total balance of all aacounts given a budget and a date range.

# Import the budget library
import budgeting_lib as bl
import datetime as dt
import argparse

# Create command line argument
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('startdate', type=str, help='Start date of the budget')
parser.add_argument('enddate', type=str, help='End date of the budget')
args = parser.parse_args()

# Convert enddate to datetime.date object where the input is given as YYYY-MM-DD
args.startdate = dt.datetime.strptime(args.startdate, '%Y-%m-%d').date()
args.enddate = dt.datetime.strptime(args.enddate, '%Y-%m-%d').date()

# Start and end dates for income and transfers (these can be changed so they are not the same)
# The income start date might be different for each income source, because of the start date is
# the day the income is earn and related to the frequency of the income source.
# Similarly is true for the transfer start date.
startdate = dt.date(2023, 1, 1)
enddate = dt.date(2023, 12, 31)

# Create bills, expenses, and incomes

# A bill has a name, amount, duedate, frequency, category, and ifweekday
bills = [   
            bl.bill(name="rent", amount=1000.00, duedate=1, frequency="monthly", category="housing", ifweekday=True),
            bl.bill(name="phone", amount=79.99, duedate=1, frequency="monthly", category="utilities", ifweekday=True),
            bl.bill(name="internet", amount=79.99, duedate=15, frequency="monthly", category="utilities", ifweekday=True),
            bl.bill(name="car insurance", amount=94.99, duedate=21, frequency="monthly", category="car", ifweekday=True),
            bl.bill(name="utilties", amount=114.99, duedate=1, frequency="monthly", category="utilities", ifweekday=True),
            bl.bill(name="student loan", amount=500.00, duedate=1, frequency="weekly", category="debt", ifweekday=True),
            bl.bill(name="health insurance", amount=116.00, duedate=1, frequency="monthly", category="health", ifweekday=True),
            bl.bill(name="charity", amount=10.00, duedate=2, frequency="monthly", category="donations", ifweekday=True),
            bl.bill(name="netflix", amount=14.99, duedate=20, frequency="monthly", category="entertainment", ifweekday=True),
            bl.bill(name="spotify", amount=9.99, duedate=20, frequency="monthly", category="entertainment", ifweekday=True),
            bl.bill(name="lightroom", amount=9.99, duedate=20, frequency="monthly", category="hobbies", ifweekday=True),
]

# An expense has a name, amount, category, and description
expenses = [
                bl.expense(name="groceries", amount=200.00, category="food", description="groceries for two weeks"),
                bl.expense(name="gas", amount=50.00, category="car", description="gas for car"),
                bl.expense(name="eating out", amount=100.00, category="food", description="eating out with friends"),
]

# An income has a name, amount, frequency, category, startdate, enddate, and ifweekday
incomes = [
                bl.income(name="paycheck", amount=3000.00, frequency="biweekly", category="income", startdate=startdate, enddate=enddate, payday=1, ifweekday=True)
]

# Create three accounts
# An account has a name, type, balance, bills, expenses, and incomes
accounts = [
                bl.account(name="checking", type="checking", balance=1000.00, bills=bills, expenses=expenses, incomes=incomes),
                bl.account(name="savings", type="savings", balance=10000.00, bills=[], expenses=[], incomes=[]),
                bl.account(name="travel", type="travel", balance=500.00, bills=[], expenses=[], incomes=[]),
]

# Create two transfers
checking_account = accounts[0]
saving_account = accounts[1]
travel_account = accounts[2]

# A transfer has a name, startdate, enddate, amount, frequency, from_account, and to_account
transfers = [
                bl.transfer(name="savings", startdate=startdate, enddate=enddate, depositday=1, amount=300.00, frequency="biweekly", from_account=checking_account, to_account=saving_account),
                bl.transfer(name="travel", startdate=startdate, enddate=enddate, depositday=1, amount=100.00, frequency="biweekly", from_account=checking_account, to_account=travel_account),
]

# Create a budget
# A budget has a name, startdate, enddate, accounts, and transfers
budget = bl.budget(name="yearly budget", startdate=args.startdate, enddate=args.enddate, accounts=accounts, transfers=transfers)

# Print the summary of the budget
print(budget.summary())

# Print the final summary of the budget
print(budget.summary_final())