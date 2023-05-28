import pytest
import datetime as dt
import math
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import budgeting_lib as bl

# Behaviors I want to test for the transfer class:
# 1. The transfer class should be able to create a transfer object with the following attributes:
#    - name
#    - amount
#    - frequency
#    - date
#    - weekday or not
#    - from account
#    - to account
# 2. The transfer class should be able to return a summary of the transfer object's attributes
# 3. The transfer class should be able to return the attributes of the transfer object
# 4. The transfer class should be able to update the attributes of the transfer object
# 5. The transfer class should be able to transfer money from one account to another

# Start with the transfer class using pytest
# Create a fixture for the bills, expenses, and incomes classes
@pytest.fixture(scope="function")
def bills_expenses_incomes():
    # Create date object for the 15th of October 2020 and for the 17th of February 2021
    date1 = dt.date(2020, 10, 15)
    date2 = dt.date(2021, 2, 17)

    # Create a list of three bills, a list of two incomes, and a list of 2 expenses
    bills = [bl.bill(name="Electricity", amount=100.00, category="Utilities", frequency="Monthly", duedate=1, ifweekday=True),
                bl.bill(name="Water", amount=50.00, category="Utilities", frequency="Monthly", duedate=1, ifweekday=True),
                bl.bill(name="Internet", amount=75.00, category="Utilities", frequency="Monthly", duedate=1, ifweekday=True)]
       
    expenses = [bl.expense(name="Groceries", amount=100.00, category="Food", description="Groceries for the week"),
                bl.expense(name="Gas", amount=50.00, category="Transportation", description="Gas for the car")]
    
    incomes = [bl.income(name="Paycheck", amount=1000.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2),
                bl.income(name="Bonus", amount=500.00, frequency="Monthly", ifweekday=False, category="Work", startdate=date1, enddate=date2)]
    
    return bills, expenses, incomes

# Create a fixture for the the transfer class
@pytest.fixture(scope="function")
def transfer(bills_expenses_incomes):
    bills, expenses, incomes = bills_expenses_incomes

    # Create date object for the 15th of October 2020 and for the 17th of February 2021
    date1 = dt.date(2020, 10, 15)
    date2 = dt.date(2021, 2, 17)

    # Create the 2 account objects
    account1 = bl.account(name="chequing", type="checking", balance=20000.00, bills=bills, expenses=expenses, incomes=incomes)
    account2 = bl.account(name="savings", type="savings", balance=10000.00, bills=bills, expenses=expenses, incomes=incomes)

    return account1, account2, date1, date2

# Test number 1: The transfer class should be able to create a transfer object with the correct attributes.
# To do this, it will need a name, start date, end date, amount, frequency, and 2 account objects
def test_transfer_create(transfer):
    account1, account2, date1, date2 = transfer

    # Create the transfer object
    transfer = bl.transfer(name="transfer", amount=1000.00, startdate=date1, enddate=date2, frequency="weekly", from_account=account1, to_account=account2)

    assert transfer.name == "transfer"
    assert transfer.amount == 1000.00
    assert transfer.startdate == date1
    assert transfer.enddate == date2
    assert transfer.frequency == "weekly"
    assert transfer.from_account == account1
    assert transfer.to_account == account2

# Test number 2: The transfer class should be able to return a summary of the transfer object's attributes
def test_transfer_summary(transfer):
    account1, account2, date1, date2 = transfer

    # Create the transfer object
    transfer = bl.transfer(name="transfer", amount=1000.00, startdate=date1, enddate=date2, frequency="weekly", from_account=account1, to_account=account2)

    # Create the summary
    summary = transfer.summary()

    # Assert that the summary is correct
    summary_expected = f'Transfer Name: transfer\nTransfer Amount: $1000.00\nTransfer Frequency: weekly\nTransfer From: chequing\nTransfer To: savings\n'
    assert summary == summary_expected

# Test number 3: The transfer class should be able to update the attributes of the transfer object
def test_transfer_update(transfer):
    account1, account2, date1, date2 = transfer

    # Create the transfer object
    transfer = bl.transfer(name="transfer", amount=1000.00, startdate=date1, enddate=date2, frequency="weekly", from_account=account1, to_account=account2)

    # Update the attributes of the transfer object
    transfer.name = "new transfer"
    transfer.amount = 2000.00
    transfer.startdate = dt.date(2020, 10, 16)
    transfer.enddate = dt.date(2021, 2, 18)
    transfer.frequency = "monthly"
    transfer.from_account = account2
    transfer.to_account = account1

    # Assert that the attributes of the transfer object have been updated
    assert transfer.name == "new transfer"
    assert transfer.amount == 2000.00
    assert transfer.startdate == dt.date(2020, 10, 16)
    assert transfer.enddate == dt.date(2021, 2, 18)
    assert transfer.frequency == "monthly"
    assert transfer.from_account == account2
    assert transfer.to_account == account1

# Test number 4: The transfer class should be able to transfer money from one account to another regularly
def test_transfer_transfer(transfer):
    account1, account2, date1, date2 = transfer

    # Create the transfer object
    transfer = bl.transfer(name="transfer", amount=1000.00, startdate=date1, enddate=date2, frequency="weekly", from_account=account1, to_account=account2)

    # Transfer the money
    transfer.transfer()

    # Assert that the money has been transferred
    assert account1.balance == 19000.00
    assert account2.balance == 11000.00