import pytest
import datetime as dt
import math
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
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
# Start with test number 1: The bill class should be able to create a bill object with the needed attributes
def test_bill():
    bill = bl.bill(name="Electricity", amount=100, category="Utilities", frequency="Monthly", duedate=1, ifweekday=False)
    assert bill.name == "electricity"
    assert bill.amount == 100
    assert bill.category == "utilities"
    assert bill.frequency == "monthly"
    assert bill.duedate == 1
    assert bill.ifweekday == False


# Test number 2: The bill class should be able to return a summary of the bill object's attributes
def test_bill_summary():
    bill_Electricity = bl.bill(name="Electricity", amount=100.00, category="Utilities", frequency="Monthly", duedate=1, ifweekday=True)
    bill_Water = bl.bill(name="Water", amount=50.00, category="Utilities", frequency="Monthly", duedate=15, ifweekday=False)
    assert bill_Electricity.summary() == "electricity is a utilities bill that is due on the 1, monthly, or the earliest week day, and costs $100.00."
    assert bill_Water.summary() == "water is a utilities bill that is due on the 15, monthly, and costs $50.00."


# Test number 3: The bill class should be able to return the attributes of the bill object
def test_bill_attributes():
    bill_Electricity = bl.bill(name="Electricity", amount=100.00, category="Utilities", frequency="Monthly", duedate=1, ifweekday=True)
    bill_Water = bl.bill(name="Water", amount=50.00, category="Utilities", frequency="Monthly", duedate=15, ifweekday=False)
    assert bill_Electricity.attributes() == ["electricity", 100.00, "utilities", "monthly", 1, True]
    assert bill_Water.attributes() == ["water", 50.00, "utilities", "monthly", 15, False]


# Test number 4: The bill class should be able to update the attributes of the bill object
def test_bill_update():
    bill_Electricity = bl.bill(name="Electricity", amount=100.00, category="Utilities", frequency="Monthly", duedate=1, ifweekday=True)
    bill_Water = bl.bill(name="Water", amount=50.00, category="Utilities", frequency="Monthly", duedate=15, ifweekday=False)
    bill_Electricity.update(name="Electricity", amount=150.00, category="Utilities", frequency="Monthly", duedate=1, ifweekday=True)
    bill_Water.update(name="Water", amount=75.00, category="Utilities", frequency="Monthly", duedate=15, ifweekday=False)
    assert bill_Electricity.attributes() == ["electricity", 150.00, "utilities", "monthly", 1, True]
    assert bill_Water.attributes() == ["water", 75.00, "utilities", "monthly", 15, False]