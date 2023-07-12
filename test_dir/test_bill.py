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


# Behaviors I want to test for the bill class:
# 1. The bill class should be able to create a bill object with the following attributes:
#    - name
#    - amount
#    - due date
#    - repeating or not
#    - frequency
#    - category
#    - Must occur on a weekday or not
# 2. The bill class should be able to return a summary of the bill object's attributes
# 3. The bill class should be able to return the attributes of the bill object
# 4. The bill class should be able to update the attributes of the bill object

# Start making the tests for the classes
# Start with the bill class using pytest

# Create fixutre with start and end dates
@pytest.fixture
def dates():
    date1 = dt.date(2020, 10, 15)
    date2 = dt.date(2021, 2, 17)
    return date1, date2

# Start with test number 1: The bill class should be able to create a bill object with the needed attributes
def test_bill(dates):
    date1, date2 = dates
    bill = bl.bill(name="Electricity", amount=100, category="Utilities", frequency="Monthly", startdate=date1, enddate=date2, duedate=1, ifweekday=False)
    assert bill.name == "electricity"
    assert bill.amount == 100
    assert bill.category == "utilities"
    assert bill.frequency == "monthly"
    assert bill.startdate == date1
    assert bill.enddate == date2
    assert bill.duedate == 1
    assert bill.ifweekday == False


# Test number 2: The bill class should be able to return a summary of the bill object's attributes
def test_bill_summary(dates):
    date1, date2 = dates
    bill_Electricity = bl.bill(name="Electricity", amount=100.00, category="Utilities", frequency="Monthly", startdate=date1, enddate=date2, duedate=1, ifweekday=True)
    bill_Water = bl.bill(name="Water", amount=50.00, category="Utilities", frequency="Monthly", startdate=date1, enddate=date2, duedate=15, ifweekday=False)
    assert bill_Electricity.summary() == "electricity is a utilities bill that is due on the 1, monthly, or the earliest week day, and costs $100.00."
    assert bill_Water.summary() == "water is a utilities bill that is due on the 15, monthly, and costs $50.00."


# Test number 3: The bill class should be able to return the attributes of the bill object
def test_bill_attributes(dates):
    date1, date2 = dates
    bill_Electricity = bl.bill(name="Electricity", amount=100.00, category="Utilities", frequency="Monthly", startdate=date1, enddate=date2, duedate=1, ifweekday=True)
    bill_Water = bl.bill(name="Water", amount=50.00, category="Utilities", frequency="Monthly", startdate=date1, enddate=date2, duedate=15, ifweekday=False)
    assert bill_Electricity.attributes() == ["electricity", 100.00, "utilities", "monthly", date1, date2, 1, True]
    assert bill_Water.attributes() == ["water", 50.00, "utilities", "monthly", date1, date2, 15, False]


# Test number 4: The bill class should be able to update the attributes of the bill object
def test_bill_update(dates):
    date1, date2 = dates
    bill_Electricity = bl.bill(name="Electricity", amount=100.00, category="Utilities", frequency="Monthly", startdate=date1, enddate=date2, duedate=1, ifweekday=True)
    bill_Water = bl.bill(name="Water", amount=50.00, category="Utilities", frequency="Monthly", startdate=date1, enddate=date2, duedate=15, ifweekday=False)

    bill_Electricity.update(name="Electricity", amount=150.00, category="Utilities", frequency="Monthly", startdate=date1, enddate=date2, duedate=1, ifweekday=True)
    bill_Water.update(name="Water", amount=75.00, category="Utilities", frequency="Monthly", startdate=date1, enddate=date2, duedate=15, ifweekday=False)

    assert bill_Electricity.attributes() == ["electricity", 150.00, "utilities", "monthly", date1, date2, 1, True]
    assert bill_Water.attributes() == ["water", 75.00, "utilities", "monthly", date1, date2, 15, False]

# Test number 5: The bill class should be able to return a list of dates that the bill is due between two dates
def test_bill_dates(dates):
    date1, date2 = dates
    bill_Electricity = bl.bill(name="Electricity", amount=100.00, category="Utilities", frequency="Biweekly", startdate=date1, enddate=date2, duedate=1, ifweekday=True)
    bill_Water = bl.bill(name="Water", amount=50.00, category="Utilities", frequency="Monthly", startdate=date1, enddate=date2, duedate=15, ifweekday=False)


    bill_Electricity_dates = bill_Electricity.duedates()
    bill_Water_dates = bill_Water.duedates()

    print(bill_Electricity_dates)
    print(bill_Water_dates)

    assert bill_Electricity_dates == [dt.date(2020, 10, 15), dt.date(2020, 10, 29), dt.date(2020, 11, 12), dt.date(2020, 11, 26), dt.date(2020, 12, 10), dt.date(2020, 12, 24), dt.date(2021, 1, 7), dt.date(2021, 1, 21), dt.date(2021, 2, 4)]
    assert bill_Water_dates == [dt.date(2020, 10, 15), dt.date(2020, 11, 15), dt.date(2020, 12, 15), dt.date(2021, 1, 15), dt.date(2021, 2, 15)]

# Test number 6: The bill class should be able to calculate the total amount spent on the bill between two dates
def test_bill_total(dates):
    date1, date2 = dates
    bill_Electricity = bl.bill(name="Electricity", amount=100.00, category="Utilities", frequency="Biweekly", startdate=date1, enddate=date2, duedate=1, ifweekday=True)
    bill_Water = bl.bill(name="Water", amount=50.00, category="Utilities", frequency="Monthly", startdate=date1, enddate=date2, duedate=15, ifweekday=False)


    bill_Electricity_total = bill_Electricity.amount_spent()
    bill_Water_total = bill_Water.amount_spent()

    print(bill_Electricity_total)
    print(bill_Water_total)

    assert bill_Electricity_total == 900.00
    assert bill_Water_total == 250.00