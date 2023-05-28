# # I am creating a test file for the budgeting library that will do unit testing on the functions
# # in the budgeting library. I will be using the pytest library to do the unit testing. 

# import pytest
# import budgeting_lib as bl
# import datetime as dt
# import math

# # Behaviors I want to test for the bill class:
# # 1. The bill class should be able to create a bill object with the following attributes:
# #    - name
# #    - amount
# #    - due date
# #    - repeating or not
# #    - frequency
# #    - category
# #    - Must occur on a weekday or not
# # 2. The bill class should be able to return a summary of the bill object's attributes
# # 3. The bill class should be able to return the attributes of the bill object
# # 4. The bill class should be able to update the attributes of the bill object


# # Behaviors I want to test for the expense class:
# # 1. The expense class should be able to create an expense object with the following attributes:
# #    - name
# #    - amount
# #    - category
# #    - description
# # 2. The expense class should be able to return a summary of the expense object's attributes
# # 3. The expense class should be able to return the attributes of the expense object
# # 4. The expense class should be able to update the attributes of the expense object
# # 5. The expense class should be able to return the the amount left to spend on the expense for a given date of the month


# # Behaviors I want to test for the income class:
# # 1. The income class should be able to create an income object with the following attributes:
# #    - name
# #    - amount
# #    - category
# #    - frequency
# #    - start date
# #    - end date
# #    - weekday or not
# # 2. The income class should be able to return a summary of the income object's attributes
# # 3. The income class should be able to return the attributes of the income object
# # 4. The income class should be able to update the attributes of the income object

# # Behaviors I want to test for the transfer class:
# # 1. The transfer class should be able to create a transfer object with the following attributes:
# #    - name
# #    - amount
# #    - frequency
# #    - date
# #    - weekday or not
# #    - from account
# #    - to account
# # 2. The transfer class should be able to return a summary of the transfer object's attributes
# # 3. The transfer class should be able to return the attributes of the transfer object
# # 4. The transfer class should be able to update the attributes of the transfer object
# # 5. The transfer class should be able to transfer money from one account to another


# # Behaviors I want to test for the account class:
# # 1. The account class should be able to create an account object with the following attributes:
# #    - name
# #    - balance
# #    - type
# #    - bills
# #    - expenses
# #    - income
# #    - transfers
# # 2. The account class should be able to return a summary of the account object's attributes
# # 3. The account class should be able to return the attributes of the account object
# # 4. The account class should be able to update the attributes of the account object
# # 5. The account class should be able to change the balance when a bill is paid
# # 6. The account class should be able to change the balance when an expense is paid
# # 7. The account class should be able to change the balance when an income is received


# # Behaviors I want to test for the budget class:
# # 1. The budget class should be able to create a budget object with the following attributes:
# #    - name
# #    - start date
# #    - end date
# #    - accounts
# # 2. The budget class should be able to return a summary of the budget object's attributes
# # 3. The budget class should be able to return the attributes of the budget object
# # 4. The budget class should be able to update the attributes of the budget object
# # 5. The budget class should be able to return the total amount of money spent on bills for a given period of time
# # 6. The budget class should be able to return the total amount of money spent on expenses for a given period of time
# # 7. The budget class should be able to return the total amount of money earned from income for a given period of time
# # 8. The budget class should be able to transfer money from one account to another regularly
# # 9. The budget class should be able to return the total amount of money transferred to other accounts for a given period of time
# # 10. The budget class should be able to return the total amount of money transferred from other accounts for a given period of time
# # 11. The budget class should be able to return the total amount of money spent for a given period of time
# # 12. The budget class should be able to return the total amount of money earned for a given period of time
# # 13. The budget class should be able to return the total amount of money transferred for a given period of time
# # 14. The budget class should be able to return the total amount of money spent on bills for a given period of time for a given category
# # 15. The budget class should be able to return the total amount of money spent on expenses for a given period of time for a given category
# # 16. The budget class should be able to return the total amount of money earned from income for a given period of time for a given category
# # 17. The budget class should be able to return the total amount of money transferred to other accounts for a given period of time for a given category
# # 18. The budget class should be able to return the total amount of money transferred from other accounts for a given period of time for a given category
# # 19. The budget class should be able to return the total amount of money spent for a given period of time for a given category
# # 20. The budget class should be able to return the total amount of money earned for a given period of time for a given category
# # 21. The budget class should be able to return the total amount of money transferred for a given period of time for a given category
# # 22. The budget class should be able to return the total amount of money spent on bills for a given period of time for a given category for a given account
# # 23. The budget class should be able to return the total amount of money spent on expenses for a given period of time for a given category for a given account
# # 24. The budget class should be able to return the total balance of all accounts for a given period of time
# # 25. The budget class should be able to return set spending limits for a given category



# # Start making the tests for the classes
# # Start with the bill class using pytest
# # Start with test number 1: The bill class should be able to create a bill object with the needed attributes
# def test_bill():
#     bill = bl.bill(name="Electricity", amount=100, category="Utilities", frequency="Monthly", duedate=1, ifweekday=False)
#     assert bill.name == "electricity"
#     assert bill.amount == 100
#     assert bill.category == "utilities"
#     assert bill.frequency == "monthly"
#     assert bill.duedate == 1
#     assert bill.ifweekday == False


# # Test number 2: The bill class should be able to return a summary of the bill object's attributes
# def test_bill_summary():
#     bill_Electricity = bl.bill(name="Electricity", amount=100.00, category="Utilities", frequency="Monthly", duedate=1, ifweekday=True)
#     bill_Water = bl.bill(name="Water", amount=50.00, category="Utilities", frequency="Monthly", duedate=15, ifweekday=False)
#     assert bill_Electricity.summary() == "electricity is a utilities bill that is due on the 1, monthly, or the earliest week day, and costs $100.00."
#     assert bill_Water.summary() == "water is a utilities bill that is due on the 15, monthly, and costs $50.00."


# # Test number 3: The bill class should be able to return the attributes of the bill object
# def test_bill_attributes():
#     bill_Electricity = bl.bill(name="Electricity", amount=100.00, category="Utilities", frequency="Monthly", duedate=1, ifweekday=True)
#     bill_Water = bl.bill(name="Water", amount=50.00, category="Utilities", frequency="Monthly", duedate=15, ifweekday=False)
#     assert bill_Electricity.attributes() == ["electricity", 100.00, "utilities", "monthly", 1, True]
#     assert bill_Water.attributes() == ["water", 50.00, "utilities", "monthly", 15, False]


# # Test number 4: The bill class should be able to update the attributes of the bill object
# def test_bill_update():
#     bill_Electricity = bl.bill(name="Electricity", amount=100.00, category="Utilities", frequency="Monthly", duedate=1, ifweekday=True)
#     bill_Water = bl.bill(name="Water", amount=50.00, category="Utilities", frequency="Monthly", duedate=15, ifweekday=False)
#     bill_Electricity.update(name="Electricity", amount=150.00, category="Utilities", frequency="Monthly", duedate=1, ifweekday=True)
#     bill_Water.update(name="Water", amount=75.00, category="Utilities", frequency="Monthly", duedate=15, ifweekday=False)
#     assert bill_Electricity.attributes() == ["electricity", 150.00, "utilities", "monthly", 1, True]
#     assert bill_Water.attributes() == ["water", 75.00, "utilities", "monthly", 15, False]



# # Start with the expense class using pytest
# # Start with test number 1: The expense class should be able to create an expense object with the needed attributes
# def test_expense():
#     expense = bl.expense(name="Groceries", amount=100.00, category="Food", description="Groceries for the week")
#     assert expense.name == "groceries"
#     assert expense.amount == 100.00
#     assert expense.category == "food"
#     assert expense.description == "groceries for the week"


# # Test number 2: The expense class should be able to return a summary of the expense object's attributes
# def test_expense_summary():
#     expense_Groceries = bl.expense(name="Groceries", amount=100.00, category="Food", description="Groceries for the week")
#     expense_Restaurant = bl.expense(name="Restaurant", amount=50.00, category="Food", description="Restaurant for the week")
#     assert expense_Groceries.summary() == "groceries is a food expense that costs $100.00 and is described as groceries for the week."
#     assert expense_Restaurant.summary() == "restaurant is a food expense that costs $50.00 and is described as restaurant for the week."


# # Test number 3: The expense class should be able to return the attributes of the expense object
# def test_expense_attributes():
#     expense_Groceries = bl.expense(name="Groceries", amount=100.00, category="Food", description="Groceries for the week")
#     expense_Restaurant = bl.expense(name="Restaurant", amount=50.00, category="Food", description="Restaurant for the week")
#     assert expense_Groceries.attributes() == ["groceries", 100.00, "food", "groceries for the week"]
#     assert expense_Restaurant.attributes() == ["restaurant", 50.00, "food", "restaurant for the week"]


# # Test number 4: The expense class should be able to update the attributes of the expense object
# def test_expense_update():
#     expense_Groceries = bl.expense(name="Groceries", amount=100.00, category="Food", description="Groceries for the week")
#     expense_Restaurant = bl.expense(name="Restaurant", amount=50.00, category="Food", description="Restaurant for the week")
#     expense_Groceries.update(name="Groceries", amount=150.00, category="Food", description="Groceries for the week")
#     expense_Restaurant.update(name="Restaurant", amount=75.00, category="Food", description="Restaurant for the week")
#     assert expense_Groceries.attributes() == ["groceries", 150.00, "food", "groceries for the week"]
#     assert expense_Restaurant.attributes() == ["restaurant", 75.00, "food", "restaurant for the week"]


# # Test number 5: The expense class should be able to return the the amount spent on the expense for a given date of the month
# def test_expense_amount_left():
#     expense_Groceries = bl.expense(name="Groceries", amount=100.00, category="Food", description="Groceries for the week")
#     expense_Restaurant = bl.expense(name="Restaurant", amount=50.00, category="Food", description="Restaurant for the week")

#     # Makes a date object for the 15th of October 2020 and for the 17th of February 2020
#     date1 = dt.date(2020, 10, 15)
#     date2 = dt.date(2020, 2, 17)

#     # The amount spent on the 15th of October 2020 for the expense_Groceries object should be a percentage of the amount of days passed for the month of October
#     amount1 = 100.00 * (15.0 / 31.0)
#     assert expense_Groceries.amount_left(date1) == amount1

#     # The amount spent on the 17th of February 2020 for the expense_Restaurant object should be a percentage of the amount of days passed for the month of February
#     amount2 = 50.00 * (17.0 / 29.0)
#     assert expense_Restaurant.amount_left(date2) == amount2



# # Start with the income class using pytest
# # Start with test number 1: The income class should be able to create an income object with the needed attributes
# def test_income():
#     # Create date object for the 15th of October 2020 and for the 17th of February 2021
#     date1 = dt.date(2020, 10, 15)
#     date2 = dt.date(2021, 2, 17)

#     income = bl.income(name="Paycheck", amount=1000.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2)
#     assert income.name == "paycheck"
#     assert income.amount == 1000.00
#     assert income.frequency == "weekly"
#     assert income.ifweekday == True
#     assert income.category == "work"
#     assert income.startdate == date1
#     assert income.enddate == date2


# # Test number 2: The income class should be able to return a summary of the income object's attributes
# def test_income_summary():
#     # Create date object for the 15th of October 2020 and for the 17th of February 2021
#     date1 = dt.date(2020, 10, 15)
#     date2 = dt.date(2021, 2, 17)

#     income_Paycheck = bl.income(name="Paycheck", amount=1000.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2)
#     income_Bonus = bl.income(name="Bonus", amount=500.00, frequency="Monthly", ifweekday=False, category="Work", startdate=date1, enddate=date2)
#     assert income_Paycheck.summary() == "paycheck is a work income that is received weekly, or the earliest week day, and is worth $1000.00."
#     assert income_Bonus.summary() == "bonus is a work income that is received monthly, and is worth $500.00."


# # Test number 3: The income class should be able to return the attributes of the income object
# def test_income_attributes():
#     # Create date object for the 15th of October 2020 and for the 17th of February 2021
#     date1 = dt.date(2020, 10, 15)
#     date2 = dt.date(2021, 2, 17)

#     income_Paycheck = bl.income(name="Paycheck", amount=1000.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2)
#     income_Bonus = bl.income(name="Bonus", amount=500.00, frequency="Monthly", ifweekday=False, category="Work", startdate=date1, enddate=date2)
#     assert income_Paycheck.attributes() == ["paycheck", 1000.00, "weekly", True, "work", date1, date2]
#     assert income_Bonus.attributes() == ["bonus", 500.00, "monthly", False, "work", date1, date2]


# # Test number 4: The income class should be able to update the attributes of the income object
# def test_income_update():
#     # Create date object for the 15th of October 2020 and for the 17th of February 2021
#     date1 = dt.date(2020, 10, 15)
#     date2 = dt.date(2021, 2, 17)

#     income_Paycheck = bl.income(name="Paycheck", amount=1000.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2)
#     income_Bonus = bl.income(name="Bonus", amount=500.00, frequency="Monthly", ifweekday=False, category="Work", startdate=date1, enddate=date2)
#     income_Paycheck.update(name="Paycheck", amount=1500.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2)
#     income_Bonus.update(name="Bonus", amount=750.00, frequency="Monthly", ifweekday=False, category="Work", startdate=date1, enddate=date2)
#     assert income_Paycheck.attributes() == ["paycheck", 1500.00, "weekly", True, "work", date1, date2]
#     assert income_Bonus.attributes() == ["bonus", 750.00, "monthly", False, "work", date1, date2]


# # Test number 5: The income class should be able to return the amount of income received for a given date of the month
# def test_income_amount():
#     # Create date object for the 15th of October 2020 and for the 17th of February 2021
#     date1 = dt.date(2020, 10, 15)
#     date2 = dt.date(2021, 2, 17)

#     income_Paycheck = bl.income(name="Paycheck", amount=1000.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2)
#     income_Bonus = bl.income(name="Bonus", amount=500.00, frequency="Monthly", ifweekday=False, category="Work", startdate=date1, enddate=date2)

#     # The amount received on the 15th of October 2020 for the income_Paycheck object should be a percentage of the amount of days passed for the month of October
#     amount1 = 1000.00 * (15.0 / 31.0)
#     assert income_Paycheck.amount_earned_month(date1) == amount1

#     # The amount received on the 17th of February 2021 for the income_Bonus object should be a percentage of the amount of days passed for the month of February
#     amount2 = 500.00 * (17.0 / 28.0)
#     assert income_Bonus.amount_earned_month(date2) == amount2

# # Test number 6: The income class should be able to return the amount of income received between two dates
# def test_income_amount_between_dates():
#     # Create date object for the 15th of October 2020 and for the 17th of February 2021
#     date1 = dt.date(2020, 10, 15)
#     date2 = dt.date(2021, 2, 17)

#     income_Paycheck = bl.income(name="Paycheck", amount=1000.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2)
#     income_Bonus = bl.income(name="Bonus", amount=500.00, frequency="Monthly", ifweekday=False, category="Work", startdate=date1, enddate=date2)

#     # The amount received between the 15th of October 2020 and the 17th of February 2021 for the income_Paycheck object should be a percentage of the amount of days passed for the month of October, November, December, January, and February
#     amount1 = 1000.00 * 18.0
#     assert income_Paycheck.amount_earned_diff(date1, date2) == amount1

#     # The amount received between the 15th of October 2020 and the 17th of February 2021 for the income_Bonus object should be a percentage of the amount of days passed for the month of October, November, December, January, and February
#     amount2 = 500.00 * 5
#     assert income_Bonus.amount_earned_diff(date1, date2) == amount2


# # Start with the account class using pytest
# # Create a fixture for functions that will be used in multiple tests
# @pytest.fixture(scope="function")
# def bills_expenses_incomes():
#     # Create date object for the 15th of October 2020 and for the 17th of February 2021
#     date1 = dt.date(2020, 10, 15)
#     date2 = dt.date(2021, 2, 17)

#     # Create a list of three bills, a list of two incomes, and a list of 2 expenses
#     bills = [bl.bill(name="Electricity", amount=100.00, category="Utilities", frequency="Monthly", duedate=1, ifweekday=True),
#                 bl.bill(name="Water", amount=50.00, category="Utilities", frequency="Monthly", duedate=1, ifweekday=True),
#                 bl.bill(name="Internet", amount=75.00, category="Utilities", frequency="Monthly", duedate=1, ifweekday=True)]
       
#     expenses = [bl.expense(name="Groceries", amount=100.00, category="Food", description="Groceries for the week"),
#                 bl.expense(name="Gas", amount=50.00, category="Transportation", description="Gas for the car")]
    
#     incomes = [bl.income(name="Paycheck", amount=1000.00, frequency="Weekly", ifweekday=True, category="Work", startdate=date1, enddate=date2),
#                 bl.income(name="Bonus", amount=500.00, frequency="Monthly", ifweekday=False, category="Work", startdate=date1, enddate=date2)]
    
#     return bills, expenses, incomes

# # Start with test number 1: The account class should be able to create an account object with the needed attributes
# def test_account(bills_expenses_incomes):
#     bills, expenses, incomes = bills_expenses_incomes
#     account = bl.account(name="chequing", type="checking", balance=20000.00, bills=bills, expenses=expenses, incomes=incomes)
#     assert account.name == "chequing"
#     assert account.type == "checking"
#     assert account.balance == 20000.00
#     assert account.bills == bills
#     assert account.expenses == expenses
#     assert account.incomes == incomes


# # Test number 2: The account class should be able to return a summary of the account object
# def test_account_summary(bills_expenses_incomes):
#     bills, expenses, incomes = bills_expenses_incomes
#     account = bl.account(name="Chequing", type="Checking", balance=20000.00, bills=bills, expenses=expenses, incomes=incomes)
    
#     # Create the expected print statement for the account object that includes details about the bills, expenses, and incomes
#     expected = "Account Name: chequing\nAccount Type: checking\nAccount Balance: $20000.00\n\nBills:\nelectricity: $100.00\nwater: $50.00\ninternet: $75.00\n\nExpenses:\ngroceries: $100.00\ngas: $50.00\n\nIncomes:\npaycheck: $1000.00\nbonus: $500.00\n"
#     assert account.summary() == expected


# # Test number 3: The account class should be able to return the attributes of the account object
# def test_account_attributes(bills_expenses_incomes):
#     bills, expenses, incomes = bills_expenses_incomes
#     account = bl.account(name="chequing", type="checking", balance=20000.00, bills=bills, expenses=expenses, incomes=incomes)
#     assert account.attributes() == ["chequing", "checking", 20000.00, bills, expenses, incomes]


# # Test number 4: The account class should be able to update the attributes of the account object
# def test_account_update(bills_expenses_incomes):
#     bills, expenses, incomes = bills_expenses_incomes
#     account = bl.account(name="chequing", type="checking", balance=20000.00, bills=bills, expenses=expenses, incomes=incomes)
#     account.update(name="savings", type="savings", balance=10000.00, bills=bills, expenses=expenses, incomes=incomes)
#     assert account.attributes() == ["savings", "savings", 10000.00, bills, expenses, incomes]


# # Test number 5: The account class should be able to return the total amount of bills, expenses, and incomes for a given date range
# def test_account_total(bills_expenses_incomes):
#     bills, expenses, incomes = bills_expenses_incomes
#     account = bl.account(name="chequing", type="checking", balance=20000.00, bills=bills, expenses=expenses, incomes=incomes)

#     # Create date object for the 15th of October 2020 and for the 17th of February 2021
#     date1 = dt.date(2020, 10, 15)
#     date2 = dt.date(2021, 2, 17)

#     # The total amount of bills for the date range should be the total per month for the months of November, December, January, and February, since the bills are due on the 1st of the month
#     # Since the bills are monthly, the total amount of bills should be the amount of bills multiplied by 4
#     bills_expected = 4 * (100.00 + 50.00 + 75.00)
#     assert account.total_bills(date1, date2) == bills_expected

#     # The total amount of expenses for the date range. We need to consider that that the date range does not start at the beginning of
#     # the month nor end at the end of the month. Therefore, we need to consider the amount of expenses that are incurred in the month of October
#     # and the month of February differently than the other months. These need to be calculated using a percentage of the total amount of expenses
#     # for the month. The total amount of expenses for the month of October is the number of days from the 10/15/2020 to the end of the month
#     # divided by the total number of days in the month. The total amount of expenses for the month of February is the number of days from the
#     # beginning of the month to the 2/17/2021 divided by the total number of days in the month. The total amount of expenses for the months of
#     # November, December, and January is the total amount of expenses for the month. The total amount of expenses for the date range is the sum
#     # of the total amount of expenses for each month
#     expenses_expected = (16/31) * (100.00 + 50.00) + 3.0*(150.00) + (17/28) * (100.00 +50.00)

#     # Assert that these number are close enough to each other
#     assert math.isclose(account.total_expenses(date1, date2), expenses_expected)

#     # The total amount of incomes for the date range. This is just the number of times the income is paid in the date range multiplied by the amount of the income
#     # The income "Paycheck" is paid weekly and it starts on the 15th of October 2020 and ends on the 17th of February 2021. Since there are 17 weeks in this date range,
#     # the total amount of income for this date range is 17 * 1000.00 = 17000.00
#     incomes_expected_paycheck = 18 * 1000.00

#     # The income "Bonus" is paid monthly and it starts on the 15th of October 2020 and ends on the 17th of February 2021. The range runs over the 15th of each month
#     # this many times: October, November, December, January, February. Therefore, the total amount of income for this date range is 5 * 500.00 = 2500.00
#     incomes_expected_bonus = 5 * 500.00

#     # The total amount of income for the date range is the sum of the total amount of income for each income
#     incomes_expected = incomes_expected_paycheck + incomes_expected_bonus
#     assert account.total_incomes(date1, date2) == incomes_expected

# # Test number 6: The account class should be able to change the balance when bills are paid, expenses are paid, and incomes are paid
# def test_account_pay(bills_expenses_incomes):
#     bills, expenses, incomes = bills_expenses_incomes
#     account = bl.account(name="chequing", type="checking", balance=20000.00, bills=bills, expenses=expenses, incomes=incomes)

#     # Create date object for the 15th of October 2020 and for the 17th of February 2021
#     date1 = dt.date(2020, 10, 15)
#     date2 = dt.date(2021, 2, 17)

#     # Pay the bills for the date range
#     account.pay_bills(date1, date2)

#     # The bills are paid on the 1st of each month. Therefore, the balance should be reduced by the total amount of bills for the date range
#     account_expected = 20000.00 - 4 * (100.00 + 50.00 + 75.00)
#     assert account.balance == account_expected

#     # Pay the expenses for the date range
#     account.pay_expenses(date1, date2)

#     # The expenses are paid on the 15th of each month. Therefore, the balance should be reduced by the total amount of expenses for the date range
#     account_expected = account_expected - (16/31) * (100.00 + 50.00) - 3.0*(150.00) - (17/28) * (100.00 +50.00)
#     # Assert that these number are close enough to each other
#     assert math.isclose(account.balance, account_expected)

#     # Pay the incomes for the date range
#     account.receive_incomes(date1, date2)

#     # The incomes are paid on the 15th of each month. Therefore, the balance should be increased by the total amount of incomes for the date range
#     account_expected = account_expected + 18 * 1000.00 + 5 * 500.00
#     # Assert that these number are close enough to each other
#     assert math.isclose(account.balance, account_expected)



# # Start with the transfer class using pytest
# # Create a fixture for the the transfer class
# @pytest.fixture(scope="function")
# def transfer(bills_expenses_incomes):
#     bills, expenses, incomes = bills_expenses_incomes

#     # Create date object for the 15th of October 2020 and for the 17th of February 2021
#     date1 = dt.date(2020, 10, 15)
#     date2 = dt.date(2021, 2, 17)

#     # Create the 2 account objects
#     account1 = bl.account(name="chequing", type="checking", balance=20000.00, bills=bills, expenses=expenses, incomes=incomes)
#     account2 = bl.account(name="savings", type="savings", balance=10000.00, bills=bills, expenses=expenses, incomes=incomes)

#     return account1, account2, date1, date2

# # Test number 1: The transfer class should be able to create a transfer object with the correct attributes.
# # To do this, it will need a name, start date, end date, amount, frequency, and 2 account objects
# def test_transfer_create(transfer):
#     account1, account2, date1, date2 = transfer

#     # Create the transfer object
#     transfer = bl.transfer(name="transfer", amount=1000.00, startdate=date1, enddate=date2, frequency="weekly", from_account=account1, to_account=account2)

#     assert transfer.name == "transfer"
#     assert transfer.amount == 1000.00
#     assert transfer.startdate == date1
#     assert transfer.enddate == date2
#     assert transfer.frequency == "weekly"
#     assert transfer.from_account == account1
#     assert transfer.to_account == account2

# # Test number 2: The transfer class should be able to return a summary of the transfer object's attributes
# def test_transfer_summary(transfer):
#     account1, account2, date1, date2 = transfer

#     # Create the transfer object
#     transfer = bl.transfer(name="transfer", amount=1000.00, startdate=date1, enddate=date2, frequency="weekly", from_account=account1, to_account=account2)

#     # Create the summary
#     summary = transfer.summary()

#     # Assert that the summary is correct
#     summary_expected = f'Transfer Name: transfer\nTransfer Amount: $1000.00\nTransfer Frequency: weekly\nTransfer From: chequing\nTransfer To: savings\n'
#     assert summary == summary_expected

# # Test number 3: The transfer class should be able to update the attributes of the transfer object
# def test_transfer_update(transfer):
#     account1, account2, date1, date2 = transfer

#     # Create the transfer object
#     transfer = bl.transfer(name="transfer", amount=1000.00, startdate=date1, enddate=date2, frequency="weekly", from_account=account1, to_account=account2)

#     # Update the attributes of the transfer object
#     transfer.name = "new transfer"
#     transfer.amount = 2000.00
#     transfer.startdate = dt.date(2020, 10, 16)
#     transfer.enddate = dt.date(2021, 2, 18)
#     transfer.frequency = "monthly"
#     transfer.from_account = account2
#     transfer.to_account = account1

#     # Assert that the attributes of the transfer object have been updated
#     assert transfer.name == "new transfer"
#     assert transfer.amount == 2000.00
#     assert transfer.startdate == dt.date(2020, 10, 16)
#     assert transfer.enddate == dt.date(2021, 2, 18)
#     assert transfer.frequency == "monthly"
#     assert transfer.from_account == account2
#     assert transfer.to_account == account1

# # Test number 4: The transfer class should be able to transfer money from one account to another regularly
# def test_transfer_transfer(transfer):
#     account1, account2, date1, date2 = transfer

#     # Create the transfer object
#     transfer = bl.transfer(name="transfer", amount=1000.00, startdate=date1, enddate=date2, frequency="weekly", from_account=account1, to_account=account2)

#     # Transfer the money
#     transfer.transfer()

#     # Assert that the money has been transferred
#     assert account1.balance == 19000.00
#     assert account2.balance == 11000.00