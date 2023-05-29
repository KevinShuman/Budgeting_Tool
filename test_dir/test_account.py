import pytest
import datetime as dt
import math
import os, sys, inspect

currentframe = inspect.currentframe()
if currentframe is not None:
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(currentframe)))
else:
    currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import budgeting_lib as bl


# Behaviors I want to test for the account class:
# 1. The account class should be able to create an account object with the following attributes:
#    - name
#    - balance
#    - type
#    - bills
#    - expenses
#    - income
#    - transfers
# 2. The account class should be able to return a summary of the account object's attributes
# 3. The account class should be able to return the attributes of the account object
# 4. The account class should be able to update the attributes of the account object
# 5. The account class should be able to change the balance when a bill is paid
# 6. The account class should be able to change the balance when an expense is paid
# 7. The account class should be able to change the balance when an income is received

# Start with the account class using pytest
# Create a fixture for functions that will be used in multiple tests
@pytest.fixture(scope="function")
def bills_expenses_incomes():
    # Create date object for the 15th of October 2020 and for the 17th of February 2021
    date1 = dt.date(2020, 10, 10)
    date2 = dt.date(2021, 2, 17)

    # Create a list of three bills, a list of two incomes, and a list of 2 expenses
    bills = [bl.bill(name="Electricity", amount=100.00, category="Utilities", frequency="Monthly", duedate=1, ifweekday=True),
                bl.bill(name="Water", amount=50.00, category="Utilities", frequency="Monthly", duedate=1, ifweekday=True),
                bl.bill(name="Internet", amount=75.00, category="Utilities", frequency="Monthly", duedate=1, ifweekday=True)]
       
    expenses = [bl.expense(name="Groceries", amount=100.00, category="Food", description="Groceries for the week"),
                bl.expense(name="Gas", amount=50.00, category="Transportation", description="Gas for the car")]
    
    incomes = [bl.income(name="Paycheck", amount=1000.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2, payday=10),
                bl.income(name="Bonus", amount=500.00, frequency="Monthly", ifweekday=False, category="Work", startdate=date1, enddate=date2, payday=10)]
    
    return bills, expenses, incomes

# Start with test number 1: The account class should be able to create an account object with the needed attributes
def test_account(bills_expenses_incomes):
    bills, expenses, incomes = bills_expenses_incomes
    account = bl.account(name="chequing", type="checking", balance=20000.00, bills=bills, expenses=expenses, incomes=incomes)
    assert account.name == "chequing"
    assert account.type == "checking"
    assert account.balance == 20000.00
    assert account.bills == bills
    assert account.expenses == expenses
    assert account.incomes == incomes


# Test number 2: The account class should be able to return a summary of the account object
def test_account_summary(bills_expenses_incomes):
    bills, expenses, incomes = bills_expenses_incomes
    account = bl.account(name="Chequing", type="Checking", balance=20000.00, bills=bills, expenses=expenses, incomes=incomes)
    
    # Create the expected print statement for the account object that includes details about the bills, expenses, and incomes
    expected = "Account Name: chequing\nAccount Type: checking\nAccount Balance: $20000.00\n\nBills:\nelectricity: $100.00\nwater: $50.00\ninternet: $75.00\n\nExpenses:\ngroceries: $100.00\ngas: $50.00\n\nIncomes:\npaycheck: $1000.00\nbonus: $500.00\n"
    assert account.summary() == expected


# Test number 3: The account class should be able to return the attributes of the account object
def test_account_attributes(bills_expenses_incomes):
    bills, expenses, incomes = bills_expenses_incomes
    account = bl.account(name="chequing", type="checking", balance=20000.00, bills=bills, expenses=expenses, incomes=incomes)
    assert account.attributes() == ["chequing", "checking", 20000.00, bills, expenses, incomes]


# Test number 4: The account class should be able to update the attributes of the account object
def test_account_update(bills_expenses_incomes):
    bills, expenses, incomes = bills_expenses_incomes
    account = bl.account(name="chequing", type="checking", balance=20000.00, bills=bills, expenses=expenses, incomes=incomes)
    account.update(name="savings", type="savings", balance=10000.00, bills=bills, expenses=expenses, incomes=incomes)
    assert account.attributes() == ["savings", "savings", 10000.00, bills, expenses, incomes]


# Test number 5: The account class should be able to return the total amount of bills, expenses, and incomes for a given date range
def test_account_total(bills_expenses_incomes):
    bills, expenses, incomes = bills_expenses_incomes
    account = bl.account(name="chequing", type="checking", balance=20000.00, bills=bills, expenses=expenses, incomes=incomes)

    # Create date object for the 15th of October 2020 and for the 17th of February 2021
    date1 = dt.date(2020, 10, 10)
    date2 = dt.date(2021, 2, 17)

    # The total amount of bills for the date range should be the total per month for the months of November, December, January, and February, since the bills are due on the 1st of the month
    # Since the bills are monthly, the total amount of bills should be the amount of bills multiplied by 4
    bills_expected = 4 * (100.00 + 50.00 + 75.00)
    assert account.total_bills(date1, date2) == bills_expected

    # The total amount of expenses for the date range. We need to consider that that the date range does not start at the beginning of
    # the month nor end at the end of the month. Therefore, we need to consider the amount of expenses that are incurred in the month of October
    # and the month of February differently than the other months. These need to be calculated using a percentage of the total amount of expenses
    # for the month. The total amount of expenses for the month of October is the number of days from the 10/15/2020 to the end of the month
    # divided by the total number of days in the month. The total amount of expenses for the month of February is the number of days from the
    # beginning of the month to the 2/17/2021 divided by the total number of days in the month. The total amount of expenses for the months of
    # November, December, and January is the total amount of expenses for the month. The total amount of expenses for the date range is the sum
    # of the total amount of expenses for each month
    expenses_expected = (21/31) * (100.00 + 50.00) + 3.0*(150.00) + (17/28) * (100.00 +50.00)

    # Assert that these number are close enough to each other
    assert math.isclose(account.total_expenses(date1, date2), expenses_expected)

    # The total amount of incomes for the date range. This is just the number of times the income is paid in the date range multiplied by the amount of the income
    # The income "Paycheck" is paid weekly and it starts on the 15th of October 2020 and ends on the 17th of February 2021. Since there are 17 weeks in this date range,
    # the total amount of income for this date range is 17 * 1000.00 = 17000.00
    incomes_expected_paycheck = 18 * 1000.00

    # The income "Bonus" is paid monthly and it starts on the 15th of October 2020 and ends on the 17th of February 2021. The range runs over the 15th of each month
    # this many times: October, November, December, January, February. Therefore, the total amount of income for this date range is 5 * 500.00 = 2500.00
    incomes_expected_bonus = 5 * 500.00

    # The total amount of income for the date range is the sum of the total amount of income for each income
    incomes_expected = incomes_expected_paycheck + incomes_expected_bonus
    assert account.total_incomes(date1, date2) == incomes_expected

# Test number 6: The account class should be able to change the balance when bills are paid, expenses are paid, and incomes are paid
def test_account_pay(bills_expenses_incomes):
    bills, expenses, incomes = bills_expenses_incomes
    account = bl.account(name="chequing", type="checking", balance=20000.00, bills=bills, expenses=expenses, incomes=incomes)

    # Create date object for the 15th of October 2020 and for the 17th of February 2021
    date1 = dt.date(2020, 10, 10)
    date2 = dt.date(2021, 2, 17)

    # Pay the bills for the date range
    account.pay_bills(date1, date2)

    # The bills are paid on the 1st of each month. Therefore, the balance should be reduced by the total amount of bills for the date range
    account_expected = 20000.00 - 4 * (100.00 + 50.00 + 75.00)
    assert account.balance == account_expected

    # Pay the expenses for the date range
    account.pay_expenses(date1, date2)

    # The expenses are paid on the 15th of each month. Therefore, the balance should be reduced by the total amount of expenses for the date range
    account_expected = account_expected - (21/31) * (100.00 + 50.00) - 3.0*(150.00) - (17/28) * (100.00 +50.00)
    # Assert that these number are close enough to each other
    assert math.isclose(account.balance, account_expected)

    # Pay the incomes for the date range
    account.receive_incomes()

    # The incomes are paid on the 15th of each month. Therefore, the balance should be increased by the total amount of incomes for the date range
    account_expected = account_expected + 18 * 1000.00 + 5 * 500.00
    # Assert that these number are close enough to each other
    assert math.isclose(account.balance, account_expected)