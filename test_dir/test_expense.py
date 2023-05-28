import pytest
import datetime as dt
import math
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import budgeting_lib as bl

# Behaviors I want to test for the expense class:
# 1. The expense class should be able to create an expense object with the following attributes:
#    - name
#    - amount
#    - category
#    - description
# 2. The expense class should be able to return a summary of the expense object's attributes
# 3. The expense class should be able to return the attributes of the expense object
# 4. The expense class should be able to update the attributes of the expense object
# 5. The expense class should be able to return the the amount left to spend on the expense for a given date of the month

# Start with test number 1: The expense class should be able to create an expense object with the needed attributes
def test_expense():
    expense = bl.expense(name="Groceries", amount=100.00, category="Food", description="Groceries for the week")
    assert expense.name == "groceries"
    assert expense.amount == 100.00
    assert expense.category == "food"
    assert expense.description == "groceries for the week"


# Test number 2: The expense class should be able to return a summary of the expense object's attributes
def test_expense_summary():
    expense_Groceries = bl.expense(name="Groceries", amount=100.00, category="Food", description="Groceries for the week")
    expense_Restaurant = bl.expense(name="Restaurant", amount=50.00, category="Food", description="Restaurant for the week")
    assert expense_Groceries.summary() == "groceries is a food expense that costs $100.00 and is described as groceries for the week."
    assert expense_Restaurant.summary() == "restaurant is a food expense that costs $50.00 and is described as restaurant for the week."


# Test number 3: The expense class should be able to return the attributes of the expense object
def test_expense_attributes():
    expense_Groceries = bl.expense(name="Groceries", amount=100.00, category="Food", description="Groceries for the week")
    expense_Restaurant = bl.expense(name="Restaurant", amount=50.00, category="Food", description="Restaurant for the week")
    assert expense_Groceries.attributes() == ["groceries", 100.00, "food", "groceries for the week"]
    assert expense_Restaurant.attributes() == ["restaurant", 50.00, "food", "restaurant for the week"]


# Test number 4: The expense class should be able to update the attributes of the expense object
def test_expense_update():
    expense_Groceries = bl.expense(name="Groceries", amount=100.00, category="Food", description="Groceries for the week")
    expense_Restaurant = bl.expense(name="Restaurant", amount=50.00, category="Food", description="Restaurant for the week")
    expense_Groceries.update(name="Groceries", amount=150.00, category="Food", description="Groceries for the week")
    expense_Restaurant.update(name="Restaurant", amount=75.00, category="Food", description="Restaurant for the week")
    assert expense_Groceries.attributes() == ["groceries", 150.00, "food", "groceries for the week"]
    assert expense_Restaurant.attributes() == ["restaurant", 75.00, "food", "restaurant for the week"]


# Test number 5: The expense class should be able to return the the amount spent on the expense for a given date of the month
def test_expense_amount_left():
    expense_Groceries = bl.expense(name="Groceries", amount=100.00, category="Food", description="Groceries for the week")
    expense_Restaurant = bl.expense(name="Restaurant", amount=50.00, category="Food", description="Restaurant for the week")

    # Makes a date object for the 15th of October 2020 and for the 17th of February 2020
    date1 = dt.date(2020, 10, 15)
    date2 = dt.date(2020, 2, 17)

    # The amount spent on the 15th of October 2020 for the expense_Groceries object should be a percentage of the amount of days passed for the month of October
    amount1 = 100.00 * (15.0 / 31.0)
    assert expense_Groceries.amount_left(date1) == amount1

    # The amount spent on the 17th of February 2020 for the expense_Restaurant object should be a percentage of the amount of days passed for the month of February
    amount2 = 50.00 * (17.0 / 29.0)
    assert expense_Restaurant.amount_left(date2) == amount2