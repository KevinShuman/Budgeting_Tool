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


# Behaviors I want to test for the income class:
# 1. The income class should be able to create an income object with the following attributes:
#    - name
#    - amount
#    - category
#    - frequency
#    - start date
#    - end date
#    - weekday or not
# 2. The income class should be able to return a summary of the income object's attributes
# 3. The income class should be able to return the attributes of the income object
# 4. The income class should be able to update the attributes of the income object
# 5. The income class should be able to return the amount of income received between two dates

# Start with the income class using pytest
# Start with test number 1: The income class should be able to create an income object with the needed attributes
def test_income():
    # Create date object for the 15th of October 2020 and for the 17th of February 2021
    date1 = dt.date(2020, 10, 15)
    date2 = dt.date(2021, 2, 17)

    income = bl.income(name="Paycheck", amount=1000.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2, payday=10)
    assert income.name == "paycheck"
    assert income.amount == 1000.00
    assert income.frequency == "weekly"
    assert income.ifweekday == True
    assert income.category == "work"
    assert income.startdate == date1
    assert income.enddate == date2


# Test number 2: The income class should be able to return a summary of the income object's attributes
def test_income_summary():
    # Create date object for the 15th of October 2020 and for the 17th of February 2021
    date1 = dt.date(2020, 10, 15)
    date2 = dt.date(2021, 2, 17)

    income_Paycheck = bl.income(name="Paycheck", amount=1000.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2, payday=10)
    income_Bonus = bl.income(name="Bonus", amount=500.00, frequency="Monthly", ifweekday=False, category="Work", startdate=date1, enddate=date2, payday=10)
    assert income_Paycheck.summary() == "paycheck is a work income that is received weekly on the 10 of the month, or the earliest week day, and is worth $1000.00."
    assert income_Bonus.summary() == "bonus is a work income that is received monthly on the 10 of the month, and is worth $500.00."


# Test number 3: The income class should be able to return the attributes of the income object
def test_income_attributes():
    # Create date object for the 15th of October 2020 and for the 17th of February 2021
    date1 = dt.date(2020, 10, 15)
    date2 = dt.date(2021, 2, 17)

    income_Paycheck = bl.income(name="Paycheck", amount=1000.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2, payday=10)
    income_Bonus = bl.income(name="Bonus", amount=500.00, frequency="Monthly", ifweekday=False, category="Work", startdate=date1, enddate=date2, payday=10)
    assert income_Paycheck.attributes() == ["paycheck", 1000.00, "weekly", True, "work", date1, date2, 10]
    assert income_Bonus.attributes() == ["bonus", 500.00, "monthly", False, "work", date1, date2, 10]


# Test number 4: The income class should be able to update the attributes of the income object
def test_income_update():
    # Create date object for the 15th of October 2020 and for the 17th of February 2021
    date1 = dt.date(2020, 10, 15)
    date2 = dt.date(2021, 2, 17)

    income_Paycheck = bl.income(name="Paycheck", amount=1000.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2, payday=10)
    income_Bonus = bl.income(name="Bonus", amount=500.00, frequency="Monthly", ifweekday=False, category="Work", startdate=date1, enddate=date2, payday=10)
    income_Paycheck.update(name="Paycheck", amount=1500.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2, payday=10)
    income_Bonus.update(name="Bonus", amount=750.00, frequency="Monthly", ifweekday=False, category="Work", startdate=date1, enddate=date2, payday=10)
    assert income_Paycheck.attributes() == ["paycheck", 1500.00, "weekly", True, "work", date1, date2, 10]
    assert income_Bonus.attributes() == ["bonus", 750.00, "monthly", False, "work", date1, date2, 10]


# Test number 5: The income class should be able to return the amount of income received between two dates
def test_income_amount():
    # Create date object for the 15th of October 2020 and for the 17th of February 2021
    date1 = dt.date(2020, 10, 10)
    date2 = dt.date(2021, 2, 17)

    income_Paycheck = bl.income(name="Paycheck", amount=1000.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2, payday=10)
    income_Bonus = bl.income(name="Bonus", amount=500.00, frequency="Monthly", ifweekday=False, category="Work", startdate=date1, enddate=date2, payday=10)

    # The amount received between the 10th of October 2020 and the 17th of February 2021 for the income_Paycheck object should be
    # the number of times the income is paid between the two dates multiplied by the amount of the income. The number of times the
    # income is paid is determined by starting on the 10th of the month and adding the frequency to the date until the end date is
    # reached.
    amount1 = 1000.00 * 18
    assert income_Paycheck.amount_earned() == amount1

    # The amount received between the 10th of October 2020 and the 17th of February 2021 for the income_Bonus object should be
    # the number of times the income is paid between the two dates multiplied by the amount of the income. The number of times the
    # income is paid is determined by starting on the 10th of the month and adding the frequency to the date until the end date is
    # reached.
    amount2 = 500.00 * 5
    assert income_Bonus.amount_earned() == amount2