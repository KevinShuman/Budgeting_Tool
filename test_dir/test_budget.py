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


# Behaviors I want to test for the budget class:
# 1. The budget class should be able to create a budget object with the following attributes:
#    - name
#    - start date
#    - end date
#    - accounts
# 2. The budget class should be able to return a summary of the budget object's attributes
# 3. The budget class should be able to return the attributes of the budget object
# 4. The budget class should be able to update the attributes of the budget object
# 5. The budget class should be able to transfer money from one account to another regularly
# 6. The budget class should be able to return the total amount of money spent for a given period of time
# 7. The budget class should be able to return the total amount of money earned for a given period of time
# 8. The budget class should be able to return the total balance of all accounts for a given period of time

# Start with the budget class using pytest
# Create a fixture for the bills, expenses, and incomes classes
@pytest.fixture(scope="function")
def bills_expenses_incomes():
    # Create date object for the 15th of October 2020 and for the 17th of February 2021
    date1 = dt.date(2020, 10, 10)
    date2 = dt.date(2021, 2, 17)

    # Create a list of three bills, a list of two incomes, and a list of 2 expenses
    bills = [bl.bill(name="Electricity", amount=100.00, category="Utilities", frequency="Monthly", startdate=date1, enddate=date2, duedate=1, ifweekday=True),
                bl.bill(name="Water", amount=50.00, category="Utilities", frequency="Monthly", startdate=date1, enddate=date2, duedate=1, ifweekday=True),
                bl.bill(name="Internet", amount=75.00, category="Utilities", frequency="Monthly", startdate=date1, enddate=date2, duedate=1, ifweekday=True)]
       
    expenses = [bl.expense(name="Groceries", amount=100.00, category="Food", description="Groceries for the week"),
                bl.expense(name="Gas", amount=50.00, category="Transportation", description="Gas for the car")]
    
    incomes = [bl.income(name="Paycheck", amount=1000.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2, payday=10),
                bl.income(name="Bonus", amount=500.00, frequency="Monthly", ifweekday=False, category="Work", startdate=date1, enddate=date2, payday=10)]
    
    return bills, expenses, incomes

# Create a fixture for the the transfer class
@pytest.fixture(scope="function")
def budget(bills_expenses_incomes):
    bills, expenses, incomes = bills_expenses_incomes

    # Create date object for the 15th of October 2020 and for the 17th of February 2021
    date1 = dt.date(2020, 10, 10)
    date2 = dt.date(2021, 2, 17)

    # Create the 2 account objects
    account1 = bl.account(name="chequing", type="checking", balance=20000.00, bills=bills, expenses=expenses, incomes=incomes)
    account2 = bl.account(name="savings", type="savings", balance=10000.00, bills=bills, expenses=expenses, incomes=incomes)

    return account1, account2, date1, date2


# Test 1: The budget class should be able to create a budget object with the correct attributes
def test_budget_create(budget):
    account1, account2, date1, date2 = budget

    # Create a budget object
    budget = bl.budget(name="test budget", startdate=date1, enddate=date2, accounts=[account1, account2], transfers=[])

    # Check that the budget object has the correct attributes
    assert budget.name == "test budget"
    assert budget.startdate == date1
    assert budget.enddate == date2
    assert budget.accounts == [account1, account2]
    assert budget.transfers == []

# Test 2: The budget class should be able to return a summary of the budget object's attributes
def test_budget_summary(budget):
    account1, account2, date1, date2 = budget

    # Create a budget object
    budget = bl.budget(name="test budget", startdate=date1, enddate=date2, accounts=[account1, account2], transfers=[])
    expected_summary = f"Budget: {budget.name}\nStart Date: {budget.startdate}\nEnd Date: {budget.enddate}\nAccounts:\n"

    for account in budget.accounts:
        expected_summary += f"{account.summary()}\n"

    for transfer in budget.transfers:
        expected_summary += f"{transfer.summary()}\n"

    # Check that the budget object has the correct summary that includes summary of the accounts using the account.summary() method
    assert budget.summary() == expected_summary

# Test 3: The budget class should be able to return the attributes of the budget object
def test_budget_attributes(budget):
    account1, account2, date1, date2 = budget

    # Create a budget object
    budget = bl.budget(name="test budget", startdate=date1, enddate=date2, accounts=[account1, account2], transfers=[])

    # Check that the budget object has the correct attributes along with those of the accounts
    assert budget.attributes() == ["test budget", date1, date2, account1.attributes(), account2.attributes()]

# Test 4: The budget class should be able to update the attributes of the budget object
def test_budget_update(budget):
    account1, account2, date1, date2 = budget

    # Create a budget object
    budget = bl.budget(name="test budget", startdate=date1, enddate=date2, accounts=[account1, account2], transfers=[])

    # Update the budget object's attributes
    budget.name = "new name"
    budget.startdate = date2
    budget.enddate = date1
    budget.accounts = [account2, account1]

    # Check that the budget object has the correct updated attributes
    assert budget.name == "new name"
    assert budget.startdate == date2
    assert budget.enddate == date1
    assert budget.accounts == [account2, account1]

# Test 5: The budget class should be able to return the total amount of money spent for a given period of time
def test_budget_total_spent(budget):
    account1, account2, date1, date2 = budget

    # Create a budget object
    budget = bl.budget(name="test budget", startdate=date1, enddate=date2, accounts=[account1, account2], transfers=[])

    # Calculate the expected total amount of money spent for a given period of time by adding the total amount
    # spent from the bills and expenses of each account
    bills_expected = 4 * (100.00 + 50.00 + 75.00)
    expenses_expected = (21/31) * (100.00 + 50.00) + 3.0*(150.00) + (17/28) * (100.00 +50.00)

    acount1_total_spent =  bills_expected + expenses_expected
    acount2_total_spent =  bills_expected + expenses_expected

    expected_total_spent = acount1_total_spent + acount2_total_spent

    # Check that the budget object returns the correct total amount of money spent for a given period of time where the values are close
    # to each other
    assert math.isclose(budget.total_spent(), expected_total_spent, rel_tol=1e-09, abs_tol=0.0)

# Test 6: The budget class should be able to return the total amount of money earned for a given period of time
def test_budget_total_earned(budget):
    account1, account2, date1, date2 = budget

    # Create a budget object
    budget = bl.budget(name="test budget", startdate=date1, enddate=date2, accounts=[account1, account2], transfers=[])

    # Calculate the expected total amount of money earned for a given period of time by adding the total amount
    # earned from the incomes of each account
    incomes_expected_paycheck = 19 * 1000.00
    incomes_expected_bonus = 5 * 500.00

    acount1_total_earned =  incomes_expected_paycheck + incomes_expected_bonus
    acount2_total_earned =  incomes_expected_paycheck + incomes_expected_bonus

    expected_total_earned = acount1_total_earned + acount2_total_earned

    # Check that the budget object returns the correct total amount of money earned for a given period of time where the values are close
    # to each other
    assert math.isclose(budget.total_earned(), expected_total_earned, rel_tol=1e-09, abs_tol=0.0)

# Test 7: The budget class should be able to transfer money from one account to another regularly
def test_budget_reaccuring_transfer(budget):
    account1, account2, date1, date2 = budget

    # Create a transfer object
    transfer = bl.transfer(name="transfer", amount=1000.00, startdate=date1, enddate=date2, depositday=20, frequency="weekly", from_account=account1, to_account=account2)

    # Original account balances
    account1_balance = account1.balance
    account2_balance = account2.balance

    # Create a budget object
    budget = bl.budget(name="test budget", startdate=date1, enddate=date2, accounts=[account1, account2], transfers=[transfer])

    # Create a regular transfer from account1 to account2
    budget.reaccuring_transfer()

    # Check that the account balances are updated correctly for the number of transfers that have occurred for the given period of time
    expected_balance1 = account1_balance - 1000.00 * 18
    expected_balance2 = account2_balance + 1000.00 * 18
    assert account1.balance == expected_balance1
    assert account2.balance == expected_balance2

# Test 8: The budget class should be able to return the total balance of all accounts after a given amount of time
def test_budget_total_balance(budget):
    account1, account2, date1, date2 = budget

    # Create a transfer object
    transfer = bl.transfer(name="transfer", amount=1000.00, startdate=date1, enddate=date2, depositday=20, frequency="weekly", from_account=account1, to_account=account2)

    # Create a budget object
    budget = bl.budget(name="test budget", startdate=date1, enddate=date2, accounts=[account1, account2], transfers=[transfer])

    # Calculate the expected total balance of all accounts after a given amount of time by adding the balance of each account
    expected_total_balance = account1.balance + account2.balance

    # Check that the budget object returns the correct total balance of all accounts after a given amount of time where the values are close
    # to each other
    assert math.isclose(budget.total_balance(), expected_total_balance, rel_tol=1e-09, abs_tol=0.0)

# Test 9: The budget class should be able to return a summary after the budget has ended, which includes the total amount of money spent, earned, and the total balance
def test_budget_summary_final(budget):
    account1, account2, date1, date2 = budget

    # Create a transfer object
    transfer = bl.transfer(name="transfer", amount=1000.00, startdate=date1, enddate=date2, depositday=20, frequency="weekly", from_account=account1, to_account=account2)

    # Create a budget object
    budget = bl.budget(name="test budget", startdate=date1, enddate=date2, accounts=[account1, account2], transfers=[transfer])

    # Copy account balances
    account1_balance = account1.balance
    account2_balance = account2.balance

    # Calculate the expected total amount of money spent for a given period of time by adding the total amount
    # spent from the bills and expenses of each account
    bills_expected = 4 * (100.00 + 50.00 + 75.00)
    expenses_expected = (21/31) * (100.00 + 50.00) + 3.0*(150.00) + (17/28) * (100.00 +50.00)

    acount1_total_spent =  bills_expected + expenses_expected
    acount2_total_spent =  bills_expected + expenses_expected

    expected_total_spent = acount1_total_spent + acount2_total_spent

    # Calculate the expected total amount of money earned for a given period of time by adding the total amount
    # earned from the incomes of each account
    incomes_expected_paycheck = 19 * 1000.00
    incomes_expected_bonus = 5 * 500.00

    acount1_total_earned =  incomes_expected_paycheck + incomes_expected_bonus
    acount2_total_earned =  incomes_expected_paycheck + incomes_expected_bonus

    expected_total_earned = acount1_total_earned + acount2_total_earned

    # Update the account balances for the spent and earned amounts
    account1_balance -= acount1_total_spent
    account2_balance -= acount2_total_spent
    account1_balance += acount1_total_earned
    account2_balance += acount2_total_earned

    # Calculate the expected total balance of all accounts after a given amount of time by adding the balance of each account
    expected_total_balance = account1_balance + account2_balance

    # Create the expected balances after the transfers have occurred
    account1_balance = account1_balance - 1000.00 * 18
    account2_balance = account2_balance + 1000.00 * 18

    # Expected summary string, including the account balances
    expected_summary = "Total spent: ${:.2f}\nTotal earned: ${:.2f}\nTotal balance: ${:.2f}\nAccount balances:\n\t{}: ${:.2f}\n\t{}: ${:.2f}\n".format(expected_total_spent, expected_total_earned, expected_total_balance, account1.name, account1_balance, account2.name, account2_balance)

    # Create a summary of the budget
    summary = budget.summary_final()

    # Check that the budget object returns the correct summary string
    assert summary == expected_summary
