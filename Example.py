# This is a test example that determines the total balance of all aacounts given a budget and a date range.

# Import the budget library
import budgeting_lib as bl
import datetime as dt

# Create bills, expenses, and incomes
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

expenses = [
                bl.expense(name="groceries", amount=200.00, category="food", description="groceries for two weeks"),
                bl.expense(name="gas", amount=50.00, category="car", description="gas for car"),
                bl.expense(name="eating out", amount=100.00, category="food", description="eating out with friends"),
]

incomes = [
                bl.income(name="paycheck", amount=3000.00, frequency="biweekly", category="income", startdate=dt.date(2023, 1, 1), enddate=dt.date(2023, 12, 31), ifweekday=True)
]

# Create three accounts
accounts = [
                bl.account(name="checking", type="checking", balance=1000.00, bills=bills, expenses=expenses, incomes=incomes),
                bl.account(name="savings", type="savings", balance=10000.00, bills=[], expenses=[], incomes=[]),
                bl.account(name="travel", type="travel", balance=500.00, bills=[], expenses=[], incomes=[]),
]

# Create two transfers
checking_account = accounts[0]
saving_account = accounts[1]
travel_account = accounts[2]

transfers = [
                bl.transfer(name="savings", startdate=dt.date(2023, 1, 1), enddate=dt.date(2023, 12, 31), amount=300.00, frequency="biweekly", from_account=checking_account, to_account=saving_account),
                bl.transfer(name="travel", startdate=dt.date(2023, 1, 1), enddate=dt.date(2023, 12, 31), amount=100.00, frequency="biweekly", from_account=checking_account, to_account=travel_account),
]

# Create a budget
budget = bl.budget(name="yearly budget", startdate=dt.date(2023, 1, 1), enddate=dt.date(2023, 12, 31), accounts=accounts, transfers=transfers)

# Print the summary of the budget
print(budget.summary())

# Print the final summary of the budget
print(budget.summary_final())