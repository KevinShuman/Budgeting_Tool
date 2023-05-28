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

# Start with the income class using pytest
# Start with test number 1: The income class should be able to create an income object with the needed attributes
def test_income():
    # Create date object for the 15th of October 2020 and for the 17th of February 2021
    date1 = dt.date(2020, 10, 15)
    date2 = dt.date(2021, 2, 17)

    income = bl.income(name="Paycheck", amount=1000.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2)
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

    income_Paycheck = bl.income(name="Paycheck", amount=1000.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2)
    income_Bonus = bl.income(name="Bonus", amount=500.00, frequency="Monthly", ifweekday=False, category="Work", startdate=date1, enddate=date2)
    assert income_Paycheck.summary() == "paycheck is a work income that is received weekly, or the earliest week day, and is worth $1000.00."
    assert income_Bonus.summary() == "bonus is a work income that is received monthly, and is worth $500.00."


# Test number 3: The income class should be able to return the attributes of the income object
def test_income_attributes():
    # Create date object for the 15th of October 2020 and for the 17th of February 2021
    date1 = dt.date(2020, 10, 15)
    date2 = dt.date(2021, 2, 17)

    income_Paycheck = bl.income(name="Paycheck", amount=1000.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2)
    income_Bonus = bl.income(name="Bonus", amount=500.00, frequency="Monthly", ifweekday=False, category="Work", startdate=date1, enddate=date2)
    assert income_Paycheck.attributes() == ["paycheck", 1000.00, "weekly", True, "work", date1, date2]
    assert income_Bonus.attributes() == ["bonus", 500.00, "monthly", False, "work", date1, date2]


# Test number 4: The income class should be able to update the attributes of the income object
def test_income_update():
    # Create date object for the 15th of October 2020 and for the 17th of February 2021
    date1 = dt.date(2020, 10, 15)
    date2 = dt.date(2021, 2, 17)

    income_Paycheck = bl.income(name="Paycheck", amount=1000.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2)
    income_Bonus = bl.income(name="Bonus", amount=500.00, frequency="Monthly", ifweekday=False, category="Work", startdate=date1, enddate=date2)
    income_Paycheck.update(name="Paycheck", amount=1500.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2)
    income_Bonus.update(name="Bonus", amount=750.00, frequency="Monthly", ifweekday=False, category="Work", startdate=date1, enddate=date2)
    assert income_Paycheck.attributes() == ["paycheck", 1500.00, "weekly", True, "work", date1, date2]
    assert income_Bonus.attributes() == ["bonus", 750.00, "monthly", False, "work", date1, date2]


# Test number 5: The income class should be able to return the amount of income received for a given date of the month
def test_income_amount():
    # Create date object for the 15th of October 2020 and for the 17th of February 2021
    date1 = dt.date(2020, 10, 15)
    date2 = dt.date(2021, 2, 17)

    income_Paycheck = bl.income(name="Paycheck", amount=1000.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2)
    income_Bonus = bl.income(name="Bonus", amount=500.00, frequency="Monthly", ifweekday=False, category="Work", startdate=date1, enddate=date2)

    # The amount received on the 15th of October 2020 for the income_Paycheck object should be a percentage of the amount of days passed for the month of October
    amount1 = 1000.00 * (15.0 / 31.0)
    assert income_Paycheck.amount_earned_month(date1) == amount1

    # The amount received on the 17th of February 2021 for the income_Bonus object should be a percentage of the amount of days passed for the month of February
    amount2 = 500.00 * (17.0 / 28.0)
    assert income_Bonus.amount_earned_month(date2) == amount2

# Test number 6: The income class should be able to return the amount of income received between two dates
def test_income_amount_between_dates():
    # Create date object for the 15th of October 2020 and for the 17th of February 2021
    date1 = dt.date(2020, 10, 15)
    date2 = dt.date(2021, 2, 17)

    income_Paycheck = bl.income(name="Paycheck", amount=1000.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2)
    income_Bonus = bl.income(name="Bonus", amount=500.00, frequency="Monthly", ifweekday=False, category="Work", startdate=date1, enddate=date2)

    # The amount received between the 15th of October 2020 and the 17th of February 2021 for the income_Paycheck object should be a percentage of the amount of days passed for the month of October, November, December, January, and February
    amount1 = 1000.00 * 18.0
    assert income_Paycheck.amount_earned_diff(date1, date2) == amount1

    # The amount received between the 15th of October 2020 and the 17th of February 2021 for the income_Bonus object should be a percentage of the amount of days passed for the month of October, November, December, January, and February
    amount2 = 500.00 * 5
    assert income_Bonus.amount_earned_diff(date1, date2) == amount2