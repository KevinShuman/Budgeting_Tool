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
    transfer = bl.transfer(name="transfer", amount=1000.00, startdate=date1, enddate=date2, depositday=20, frequency="weekly", from_account=account1, to_account=account2)

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
    transfer = bl.transfer(name="transfer", amount=1000.00, startdate=date1, enddate=date2, depositday=20, frequency="weekly", from_account=account1, to_account=account2)

    # Create the summary
    summary = transfer.summary()

    # Assert that the summary is correct
    summary_expected = f'Transfer Name: transfer\nTransfer Amount: $1000.00\nTransfer Frequency: weekly\nTransfer From: chequing\nTransfer To: savings\n'
    assert summary == summary_expected

# Test number 3: The transfer class should be able to return the attributes of the transfer object
def test_transfer_attributes(transfer):
    account1, account2, date1, date2 = transfer

    # Create the transfer object
    transfer = bl.transfer(name="transfer", amount=1000.00, startdate=date1, enddate=date2, depositday=20, frequency="weekly", from_account=account1, to_account=account2)

    # Create the attributes
    attributes = transfer.attributes()

    # Assert that the list attributes are correct
    attributes_expected = ["transfer", 1000.00, date1, date2, 20, "weekly", account1, account2]
    assert attributes == attributes_expected

# Test number 4: The transfer class should be able to update the attributes of the transfer object
def test_transfer_update(transfer):
    account1, account2, date1, date2 = transfer

    # Create the transfer object
    transfer = bl.transfer(name="transfer", amount=1000.00, startdate=date1, enddate=date2, depositday=20, frequency="weekly", from_account=account1, to_account=account2)

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

# Test number 5: The transfer class should be able to transfer money from one account to another
def test_transfer_transfer(transfer):
    account1, account2, date1, date2 = transfer

    # Create the transfer object
    transfer = bl.transfer(name="transfer", amount=1000.00, startdate=date1, enddate=date2, depositday=20, frequency="weekly", from_account=account1, to_account=account2)

    # Transfer the money
    transfer.transfer()

    # Assert that the money has been transferred
    assert account1.balance == 19000.00
    assert account2.balance == 11000.00

# Test number 6: The transfer class should be able to find the dates that the transfer will occur on
#                given a start date, end date, tranfer date, and frequency. There are several cases to consider:
#                1. The transfer date is before the start date
#                2. The transfer date is after the end date
#                3. The transfer date is on the start date
#                4. The transfer date is on the end date
#                5. The transfer date is between the start date and end date
def test_transfer_deposit_days(transfer):
    account1, account2, date1, date2 = transfer

    # date1 = dt.date(2020, 10, 15)
    # date2 = dt.date(2021, 2, 17)

    # Create the transfer object with deposit day for each of the cases above
    # Case 1 - deposit day is before the start date
    transfer1 = bl.transfer(name="transfer", amount=1000.00, startdate=date1, enddate=date2, depositday=10, frequency="weekly", from_account=account1, to_account=account2)

    # Case 2 - deposit day is after the end date
    transfer2 = bl.transfer(name="transfer", amount=1000.00, startdate=date1, enddate=date2, depositday=20, frequency="weekly", from_account=account1, to_account=account2)

    # Case 3 - deposit day is on the start date
    transfer3 = bl.transfer(name="transfer", amount=1000.00, startdate=date1, enddate=date2, depositday=15, frequency="weekly", from_account=account1, to_account=account2)

    # Case 4 - deposit day is on the end date
    transfer4 = bl.transfer(name="transfer", amount=1000.00, startdate=date1, enddate=date2, depositday=17, frequency="weekly", from_account=account1, to_account=account2)

    # Case 5 - deposit day is between the start date and end date
    transfer5 = bl.transfer(name="transfer", amount=1000.00, startdate=date1, enddate=date2, depositday=16, frequency="weekly", from_account=account1, to_account=account2)


    # Create the transfer dates
    transfer_dates_1 = transfer1.deposit_days()
    transfer_dates_2 = transfer2.deposit_days()
    transfer_dates_3 = transfer3.deposit_days()
    transfer_dates_4 = transfer4.deposit_days()
    transfer_dates_5 = transfer5.deposit_days()

    # Create all the expected transfer dates for each of the cases above
    # Case 1 - deposit day is before the start date
    transfer_dates_expected_1 = [dt.date(2020, 10, 17), dt.date(2020, 10, 24), dt.date(2020, 10, 31), dt.date(2020, 11, 7), dt.date(2020, 11, 14), dt.date(2020, 11, 21), dt.date(2020, 11, 28), dt.date(2020, 12, 5), dt.date(2020, 12, 12), dt.date(2020, 12, 19), dt.date(2020, 12, 26), dt.date(2021, 1, 2), dt.date(2021, 1, 9), dt.date(2021, 1, 16), dt.date(2021, 1, 23), dt.date(2021, 1, 30), dt.date(2021, 2, 6), dt.date(2021, 2, 13)]

    # Case 2 - deposit day is after the end date
    transfer_dates_expected_2 = [dt.date(2020, 10, 20), dt.date(2020, 10, 27), dt.date(2020, 11, 3), dt.date(2020, 11, 10), dt.date(2020, 11, 17), dt.date(2020, 11, 24), dt.date(2020, 12, 1), dt.date(2020, 12, 8), dt.date(2020, 12, 15), dt.date(2020, 12, 22), dt.date(2020, 12, 29), dt.date(2021, 1, 5), dt.date(2021, 1, 12), dt.date(2021, 1, 19), dt.date(2021, 1, 26), dt.date(2021, 2, 2), dt.date(2021, 2, 9), dt.date(2021, 2, 16)]

    # Case 3 - deposit day is on the start date
    transfer_dates_expected_3 = [dt.date(2020, 10, 15), dt.date(2020, 10, 22), dt.date(2020, 10, 29), dt.date(2020, 11, 5), dt.date(2020, 11, 12), dt.date(2020, 11, 19), dt.date(2020, 11, 26), dt.date(2020, 12, 3), dt.date(2020, 12, 10), dt.date(2020, 12, 17), dt.date(2020, 12, 24), dt.date(2020, 12, 31), dt.date(2021, 1, 7), dt.date(2021, 1, 14), dt.date(2021, 1, 21), dt.date(2021, 1, 28), dt.date(2021, 2, 4), dt.date(2021, 2, 11)]

    # Case 4 - deposit day is on the end date
    transfer_dates_expected_4 = [dt.date(2020, 10, 17), dt.date(2020, 10, 24), dt.date(2020, 10, 31), dt.date(2020, 11, 7), dt.date(2020, 11, 14), dt.date(2020, 11, 21), dt.date(2020, 11, 28), dt.date(2020, 12, 5), dt.date(2020, 12, 12), dt.date(2020, 12, 19), dt.date(2020, 12, 26), dt.date(2021, 1, 2), dt.date(2021, 1, 9), dt.date(2021, 1, 16), dt.date(2021, 1, 23), dt.date(2021, 1, 30), dt.date(2021, 2, 6), dt.date(2021, 2, 13)]

    # Case 5 - deposit day is between the start date and end date
    transfer_dates_expected_5 = [dt.date(2020, 10, 16), dt.date(2020, 10, 23), dt.date(2020, 10, 30), dt.date(2020, 11, 6), dt.date(2020, 11, 13), dt.date(2020, 11, 20), dt.date(2020, 11, 27), dt.date(2020, 12, 4), dt.date(2020, 12, 11), dt.date(2020, 12, 18), dt.date(2020, 12, 25), dt.date(2021, 1, 1), dt.date(2021, 1, 8), dt.date(2021, 1, 15), dt.date(2021, 1, 22), dt.date(2021, 1, 29), dt.date(2021, 2, 5), dt.date(2021, 2, 12)]

    # Find the difference between the transfer dates and the expected transfer dates for each case
    transfer_dates_1_diff = [transfer_dates_1[i] - transfer_dates_expected_1[i] for i in range(len(transfer_dates_1))]
    transfer_dates_2_diff = [transfer_dates_2[i] - transfer_dates_expected_2[i] for i in range(len(transfer_dates_2))]
    transfer_dates_3_diff = [transfer_dates_3[i] - transfer_dates_expected_3[i] for i in range(len(transfer_dates_3))]
    transfer_dates_4_diff = [transfer_dates_4[i] - transfer_dates_expected_4[i] for i in range(len(transfer_dates_4))]
    transfer_dates_5_diff = [transfer_dates_5[i] - transfer_dates_expected_5[i] for i in range(len(transfer_dates_5))]

    # Assert that the transfer dates are correct
    assert transfer_dates_1 == transfer_dates_expected_1
    assert transfer_dates_2 == transfer_dates_expected_2
    assert transfer_dates_3 == transfer_dates_expected_3
    assert transfer_dates_4 == transfer_dates_expected_4
    assert transfer_dates_5 == transfer_dates_expected_5