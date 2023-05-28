# Import the necessary modules
import numpy as np
import datetime as dt
import time
import calendar
import math
from dateutil.relativedelta import relativedelta
from datetime import timedelta

# Define the bill class
class bill:
    # Define the initialization function
    def __init__(self, name, amount, frequency, duedate, ifweekday, category):
        '''
            This function initializes the bill object's attributes.
        
            Attributes:
                name (str): The name of the bill object.
                amount (float): The amount of money the bill object is worth.
                frequency (str): The frequency at which the bill object is due.
                duedate (int): The date the bill object is due.
                ifweekday (bool): Whether or not the bill object is due on the earliest weekday.
                category (str): The category of the bill object.
        '''

        self.name = name.lower()
        self.amount = amount
        self.category = category.lower()
        self.frequency = frequency.lower()
        self.duedate = duedate
        self.ifweekday = ifweekday

    # Define the summary function
    def summary(self):
        '''
        This function returns a summary of the bill object's attributes.
        '''
        if self.ifweekday == True:
            return f'{self.name} is a {self.category} bill that is due on the {self.duedate}, {self.frequency}, or the earliest week day, and costs ${self.amount:.2f}.'
        else:
            return f'{self.name} is a {self.category} bill that is due on the {self.duedate}, {self.frequency}, and costs ${self.amount:.2f}.'
        
    def attributes(self):
        '''
        This function returns a list of the bill object's attributes.
        '''
        return [self.name, self.amount, self.category, self.frequency, self.duedate, self.ifweekday]
    
    def update(self, name, amount, frequency, duedate, ifweekday, category):
        '''
        This function updates the bill object's attributes.
        '''
        self.name = name.lower()
        self.amount = amount
        self.category = category.lower()
        self.frequency = frequency.lower()
        self.duedate = duedate
        self.ifweekday = ifweekday

    # Calculate the amount spent on the bill object in the date range
    def amount_spent(self, startdate, enddate):
        '''
        This function calculates the amount of money spent on the bill object in the date range.
        '''
        # Calculate the number of days in the date range
        num_days = (enddate - startdate).days + 1

        # Calculate the number of times the bill object has been paid in the date range for different types of frequencies
        if self.frequency == 'weekly':
            num_times_paid = math.floor(num_days / 7)
        elif self.frequency == 'biweekly':
            num_times_paid = math.floor(num_days / 14)
        elif self.frequency == 'monthly':
            num_times_paid = math.floor(num_days / 30)
        elif self.frequency == 'bimonthly':
            num_times_paid = math.floor(num_days / 60)
        elif self.frequency == 'quarterly':
            num_times_paid = math.floor(num_days / 90)
        elif self.frequency == 'semiannually':
            num_times_paid = math.floor(num_days / 180)
        elif self.frequency == 'yearly':
            num_times_paid = math.floor(num_days / 365)
        else:
            num_times_paid = 0

        # Calculate the amount of money spent on the bill object in the date range
        amount_spent = num_times_paid * self.amount

        # Return the amount of money spent on the bill object in the date range
        return amount_spent

# Define the expense class
class expense:
    # Define the initialization function
    def __init__(self, name, amount, category, description):
        '''
            This function initializes the expense object's attributes.

            Attributes:
                name (str): The name of the expense object.
                amount (float): The amount of money the expense object is worth.
                category (str): The category of the expense object.
                description (str): The description of the expense object.
        '''

        self.name = name.lower()
        self.amount = amount
        self.category = category.lower()
        self.description = description.lower()

    # Define the summary function
    def summary(self):
        '''
        This function returns a summary of the expense object's attributes.
        '''
        return f'{self.name} is a {self.category} expense that costs ${self.amount:.2f} and is described as {self.description}.'
    
    def attributes(self):
        '''
        This function returns a list of the expense object's attributes.
        '''
        return [self.name, self.amount, self.category, self.description]
    
    def update(self, name, amount, category, description):
        '''
        This function updates the expense object's attributes.
        '''
        self.name = name.lower()
        self.amount = amount
        self.category = category.lower()
        self.description = description.lower()

    def amount_left(self, date):
        '''
        This function calculates the amount of money spent on the expense object so far in the month from a percentage of the month that has passed.
        '''
        
        # Create a datetime object for the first day of the month
        first_day = dt.date(date.year, date.month, 1)

        # Create a datetime object for the last day of the month
        last_day = dt.date(date.year, date.month, calendar.monthrange(date.year, date.month)[1])

        # Calculate the number of days in the month
        num_days = (last_day - first_day).days + 1

        # Calculate the number of days that have passed in the month
        days_passed = (date - first_day).days + 1

        # Calculate the percentage of the month that has passed
        percent_passed = days_passed / num_days

        # Calculate the amount of money spent on the expense object so far in the month
        amount_spent = self.amount * percent_passed

        # Return the amount of money spent on the expense object so far in the month
        return amount_spent
    
    def amount_spent(self, startdate, enddate):
        '''
        This function calculates the amount of money spent on the expense object in the date range. Each month gives
        a different rate per day for the expense object. For each full month in the date range, the amount spent is
        the total amount of the expense object. For the partial month at the beginning of the date range, the amount
        spent is the amount spent in the partial month. For the partial month at the end of the date range, the amount
        spent is the amount spent in the partial month. The amount spent in a partial month is calculated by multiplying
        the amount of the expense object by the percentage of the month that has passed during the date range.
        '''

        # Determine the number of days in the first month of the date range
        num_days_first_month = (dt.date(startdate.year, startdate.month, calendar.monthrange(startdate.year, startdate.month)[1]) - startdate).days + 1

        # What is the first day of the start date month?
        start_date_first_day = dt.date(startdate.year, startdate.month, 1)

        # What is the last day of the start date month?
        start_date_last_day = dt.date(startdate.year, startdate.month, calendar.monthrange(startdate.year, startdate.month)[1])

        # How many days is that?
        start_date_num_days = (start_date_last_day - start_date_first_day).days + 1

        # What is the percentage of the month that has passed?
        start_date_percent_passed = (start_date_last_day - startdate).days / start_date_num_days

        # What is the amount spent in the start date month?
        start_date_amount_spent = self.amount * start_date_percent_passed

        # Determine the number of days in the last month of the date range
        num_days_last_month = (enddate - dt.date(enddate.year, enddate.month, 1)).days + 1

        # What is the first day of the end date month?
        end_date_first_day = dt.date(enddate.year, enddate.month, 1)

        # What is the last day of the end date month?
        end_date_last_day = dt.date(enddate.year, enddate.month, calendar.monthrange(enddate.year, enddate.month)[1])

        # How many days is that?
        end_date_num_days = (end_date_last_day - end_date_first_day).days + 1

        # What is the percentage of the month that has passed?
        end_date_percent_passed = ((enddate - end_date_first_day).days + 1) / end_date_num_days

        # What is the amount spent in the end date month?
        end_date_amount_spent = self.amount * end_date_percent_passed

        # Determine the number of full months in the date range
        num_full_months = (enddate.year - startdate.year) * 12 + (enddate.month - startdate.month) - 1

        # Calculate the amount of money spent on the expense object in the date range
        amount_spent = num_full_months * self.amount + start_date_amount_spent + end_date_amount_spent

        # Return the amount of money spent on the expense object in the date range
        return amount_spent
    
    
# Define the income class
class income:
    # Define the initialization function
    def __init__(self, name, amount, frequency, ifweekday, category, startdate, enddate):
        '''
            This function initializes the income object's attributes.

            Attributes:
                name (str): The name of the income object.
                amount (float): The amount of money the income object is worth.
                frequency (str): The frequency at which the income object is received.
                ifweekday (bool): Whether or not the income object is received on the earliest weekday.
                category (str): The category of the income object.
                startdate (datetime): The date the income object starts.
                enddate (datetime): The date the income object ends.
        '''

        self.name = name.lower()
        self.amount = amount
        self.frequency = frequency.lower()
        self.ifweekday = ifweekday
        self.category = category.lower()
        self.startdate = startdate
        self.enddate = enddate

    # Define the summary function
    def summary(self):
        '''
        This function returns a summary of the income object's attributes.
        '''
        if self.ifweekday == True:
            return f'{self.name} is a {self.category} income that is received {self.frequency}, or the earliest week day, and is worth ${self.amount:.2f}.'
        else:
            return f'{self.name} is a {self.category} income that is received {self.frequency}, and is worth ${self.amount:.2f}.'
        

    def attributes(self):
        '''
        This function returns a list of the income object's attributes.
        '''
        return [self.name, self.amount, self.frequency, self.ifweekday, self.category, self.startdate, self.enddate]
    
    def update(self, name, amount, frequency, ifweekday, category, startdate, enddate):
        '''
        This function updates the income object's attributes.
        '''
        self.name = name.lower()
        self.amount = amount
        self.frequency = frequency.lower()
        self.ifweekday = ifweekday
        self.category = category.lower()
        self.startdate = startdate
        self.enddate = enddate

    def amount_earned_month(self, date):
        '''
        This function calculates the amount of money received from the income object so far in the month from a percentage of the month that has passed.
        '''
        
        # Create a datetime object for the first day of the month
        first_day = dt.date(date.year, date.month, 1)

        # Create a datetime object for the last day of the month
        last_day = dt.date(date.year, date.month, calendar.monthrange(date.year, date.month)[1])

        # Calculate the number of days in the month
        num_days = (last_day - first_day).days + 1

        # Calculate the number of days that have passed in the month
        days_passed = (date - first_day).days + 1

        # Calculate the percentage of the month that has passed
        percent_passed = days_passed / num_days

        # Calculate the amount of money received from the income object so far in the month
        amount_received = self.amount * percent_passed

        # Return the amount of money received from the income object so far in the month
        return amount_received
    
    def amount_earned_diff(self, startdate, enddate):
        '''
        This function returns the amount of money earned on the income object in the date range.
        This looks for how many times the amount is paid in a given date range and multiplies that by the amount.

        Attributes:
            startdate (datetime): The date the date range starts.
            enddate (datetime): The date the date range ends.
        '''

        # The income start date and the income frequency
        income_start_date = self.startdate
        income_frequency = self.frequency

        # Determine the date for each income payment in the date range
        income_dates = []
        if income_frequency == 'daily':
            # If the income is daily, then the income is paid every day
            income_dates = [income_start_date + dt.timedelta(days=x) for x in range((enddate - income_start_date).days + 1)]
        elif income_frequency == 'weekly':
            # If the income is weekly, then the income is paid every 7 days
            income_dates = [income_start_date + dt.timedelta(days=x) for x in range((enddate - income_start_date).days + 1) if x % 7 == 0]
        elif income_frequency == 'biweekly':
            # If the income is biweekly, then the income is paid every 14 days
            income_dates = [income_start_date + dt.timedelta(days=x) for x in range((enddate - income_start_date).days + 1) if x % 14 == 0]
        elif income_frequency == 'monthly':
            # If the income is monthly, then the income is paid every month
            income_dates = [income_start_date + relativedelta(months=x) for x in range(0, (enddate.year - income_start_date.year) * 12 + (enddate.month - income_start_date.month) + 1)]
        elif income_frequency == 'yearly':
            # If the income is yearly, then the income is paid every year
            income_dates = [income_start_date + relativedelta(years=x) for x in range(0, enddate.year - income_start_date.year + 1)]

        # Determine the number of income payments in the date range
        num_income_payments = len(income_dates)

        # Calculate the amount of money earned on the income object in the date range
        amount_earned = num_income_payments * self.amount

        # Return the amount of money earned on the income object in the date range
        return amount_earned
    
# Define the account class
class account:
    # Define the initialization function
    def __init__(self, name, type, balance, bills, expenses, incomes):
        '''
            This function initializes the account object's attributes.

            Attributes:
                name (str): The name of the account object.
                type (str): The type of the account object.
                balance (float): The balance of the account object.
                bills (list): The list of bill objects of the account object.
                expenses (list): The list of expense objects of the account object.
                incomes (list): The list of income objects of the account object.
        '''

        self.name = name.lower()
        self.type = type.lower()
        self.balance = balance
        self.bills = bills
        self.expenses = expenses
        self.incomes = incomes

    # Define the summary function
    def summary(self):
        '''
        This function returns a summary of the account object's attributes.
        '''
        
        # Creates string for the account object's attributes
        account_summary = f'Account Name: {self.name}\nAccount Type: {self.type}\nAccount Balance: ${self.balance:.2f}\n\nBills:\n'

        # Adds the summary of each bill object to the account_summary string
        for bill in self.bills:
            account_summary += f'{bill.name}: ${bill.amount:.2f}\n'

        # Adds the summary of each expense object to the account_summary string
        account_summary += '\nExpenses:\n'
        for expense in self.expenses:
            account_summary += f'{expense.name}: ${expense.amount:.2f}\n'

        # Adds the summary of each income object to the account_summary string
        account_summary += '\nIncomes:\n'
        for income in self.incomes:
            account_summary += f'{income.name}: ${income.amount:.2f}\n'

        # Returns the account_summary string
        return account_summary

    # Define the attributes function
    def attributes(self):
        '''
        This function returns a list of the account object's attributes.
        '''
        return [self.name, self.type, self.balance, self.bills, self.expenses, self.incomes]
    
    # Define the update function
    def update(self, name, type, balance, bills, expenses, incomes):
        '''
        This function updates the account object's attributes.
        '''
        self.name = name.lower()
        self.type = type
        self.balance = balance
        self.bills = bills
        self.expenses = expenses
        self.incomes = incomes

    # Define the total_bills function for a date range
    def total_bills(self, startdate, enddate):
        '''
        This function calculates the total amount of money spent on bills in a date range.
        '''
        # Initialize the total amount spent on bills to 0
        total_spent = 0

        # Iterate through each bill object in the account object
        for bill in self.bills:
            # Calculate the amount spent on the bill object in the date range
            total_spent += bill.amount_spent(startdate, enddate)

        # Return the total amount spent on bills in the date range
        return total_spent
    
    # Define the total_expenses function for a date range
    def total_expenses(self, startdate, enddate):
        '''
        This function calculates the total amount of money spent on expenses in a date range.
        '''
        # Initialize the total amount spent on expenses to 0
        total_spent = 0

        # Iterate through each expense object in the account object
        for expense in self.expenses:
            # Calculate the amount spent on the expense object in the date range
            total_spent += expense.amount_spent(startdate, enddate)

        # Return the total amount spent on expenses in the date range
        return total_spent
    
    # Define the total_incomes function for a date range
    def total_incomes(self, startdate, enddate):
        '''
        This function calculates the total amount of money received from incomes in a date range.
        '''
        # Initialize the total amount received from incomes to 0
        total_received = 0

        # Iterate through each income object in the account object
        for income in self.incomes:
            # Calculate the amount received from the income object in the date range
            total_received += income.amount_earned_diff(startdate, enddate)

        # Return the total amount received from incomes in the date range
        return total_received
    
    # Define the pay_bills function for a date range
    def pay_bills(self, startdate, enddate):
        '''
        This function pays all the bills in the account object in a date range.
        '''
        # Iterate through each bill object in the account object and determine the total amount spent on the bill object in the date range
        for bill in self.bills:
            # Calculate the amount spent on the bill object in the date range
            amount_spent = bill.amount_spent(startdate, enddate)

            # Subtract the amount spent on the bill object in the date range from the account object's balance
            self.balance -= amount_spent

    # Define the pay_expenses function for a date range
    def pay_expenses(self, startdate, enddate):
        '''
        This function pays all the expenses in the account object in a date range.
        '''
        # Iterate through each expense object in the account object and determine the total amount spent on the expense object in the date range
        for expense in self.expenses:
            # Calculate the amount spent on the expense object in the date range
            amount_spent = expense.amount_spent(startdate, enddate)

            # Subtract the amount spent on the expense object in the date range from the account object's balance
            self.balance -= amount_spent

    # Define the receive_incomes function for a date range
    def receive_incomes(self, startdate, enddate):
        '''
        This function receives all the incomes in the account object in a date range.
        '''
        # Iterate through each income object in the account object and determine the total amount received from the income object in the date range
        for income in self.incomes:
            # Calculate the amount received from the income object in the date range
            amount_received = income.amount_earned_diff(startdate, enddate)

            # Add the amount received from the income object in the date range to the account object's balance
            self.balance += amount_received

    
    
# Define transfer class
class transfer:
    # Define the initialization function
    def __init__(self, name, amount, startdate, enddate, frequency, from_account, to_account):
        '''
            This function initializes the transfer object's attributes.

            Attributes:
                name (str): The name of the transfer object.
                startdate (datetime): The date of the transfer object.
                enddate (datetime): The date of the transfer object.
                amount (float): The amount of the transfer object.
                frequency (str): The frequency of the transfer object.
                from_account (account): The account object the transfer object is from.
                to_account (account): The account object the transfer object is to.
        '''
        self.name = name.lower()    
        self.amount = amount
        self.startdate = startdate
        self.enddate = enddate
        self.frequency = frequency.lower()
        self.from_account = from_account
        self.to_account = to_account

    # Define the summary function  
    def summary(self):
        '''
        This function returns a string of the transfer object's attributes.
        '''
        # Creates string for the transfer object's attributes
        transfer_summary = f'Transfer Name: {self.name}\nTransfer Amount: ${self.amount:.2f}\nTransfer Frequency: {self.frequency}\nTransfer From: {self.from_account.name}\nTransfer To: {self.to_account.name}\n'

        # Returns the transfer_summary string
        return transfer_summary
        
    # Define the update function
    def update(self, name, amount, startdate, enddate, frequency, from_account, to_account):
        '''
        This function updates the transfer object's attributes.
        '''
        self.name = name.lower()
        self.amount = amount
        self.startdate = startdate
        self.enddate = enddate
        self.frequency = frequency.lower()
        self.from_account = from_account
        self.to_account = to_account

    # Define the transfer function
    def transfer(self):
        '''
        This function transfers money from one account object to another account object in a date range.
        It uses the account update function to update the account objects' balances. 
        '''

        # Uses the transfer amount to update the from_account object's balance
        self.from_account.balance -= self.amount

        # Uses the transfer amount to update the to_account object's balance
        self.to_account.balance += self.amount


# Define the budget class
class budget:
    '''
        This class creates a budget object.

        Attributes:
            name (str): The name of the budget object.
            startdate (datetime): The date of the budget object.
            enddate (datetime): The date of the budget object.
            account (account): The account object the budget object is for.
    '''
    # Define the initialization function
    def __init__(self, name, startdate, enddate, accounts, transfers):
        '''
            This function initializes the budget object's attributes.

            Attributes:
                name (str): The name of the budget object.
                startdate (datetime): The date of the budget object.
                enddate (datetime): The date of the budget object.
                account (list): The list of account objects the budget object is for.
                transfers (list): The list of transfer objects the budget object is for.
        '''
        self.name = name.lower()
        self.startdate = startdate
        self.enddate = enddate
        self.accounts = accounts
        self.transfers = transfers

    # Define the summary function
    def summary(self):
        '''
        This function returns a string of the budget object's attributes.
        '''
        # Creates string for the budget object's attributes
        # f"Budget:             {budget.name}\nStart Date: {budget.startdate}\nEnd Date: {budget.enddate}\nAccounts:\n{account1.summary()}\n{account2.summary()}"
        budget_summary = f'Budget: {self.name}\nStart Date: {self.startdate}\nEnd Date: {self.enddate}\nAccounts:\n'

        # Iterate through each account object in the budget object
        for account in self.accounts:
            # Add the account object's summary to the budget_summary string
            budget_summary += account.summary() + '\n'

        for transfer in self.transfers:
            # Add the transfer object's summary to the budget_summary string
            budget_summary += transfer.summary() + '\n'

        # Returns the budget_summary string
        return budget_summary
    
    # Define the attributes function
    def attributes(self):
        '''
        This function returns a list of the budget object's attributes.
        '''
        # Creates list for the budget object's attributes
        budget_attributes = [self.name, self.startdate, self.enddate]

        # Iterate through each account object in the budget object
        for account in self.accounts:
            # Add the account object's attributes to the budget_attributes list
            budget_attributes.append(account.attributes())

        for transfer in self.transfers:
            # Add the transfer object's attributes to the budget_attributes list
            budget_attributes.append(transfer.attributes())

        # Returns the budget_attributes list
        return budget_attributes
    
    # Define the update function
    def update(self, name, startdate, enddate, accounts):
        '''
        This function updates the budget object's attributes.
        '''
        self.name = name.lower()
        self.startdate = startdate
        self.enddate = enddate
        self.accounts = accounts

    # Define the total_spent function
    def total_spent(self):
        '''
        This function returns the total amount spent in the budget object in a date range.
        '''
        # Initialize the total_spent variable
        total_spent = 0

        # Iterate through each account object in the budget object
        for account in self.accounts:
            # Add the amount spent in the account object in the date range to the total_spent variable
            total_spent += account.total_bills(self.startdate, self.enddate)
            total_spent += account.total_expenses(self.startdate, self.enddate)

        # Returns the total_spent variable
        return total_spent

    # Define the total_earned function
    def total_earned(self):
        '''
        This function returns the total amount earned in the budget object in a date range.
        '''
        # Initialize the total_earned variable
        total_earned = 0

        # Iterate through each account object in the budget object
        for account in self.accounts:
            # Add the amount earned in the account object in the date range to the total_earned variable
            total_earned += account.total_incomes(self.startdate, self.enddate)

        # Returns the total_earned variable
        return total_earned
    
    # Define the test_budget_regular_transfer function
    def regular_transfer(self, transfer):
        '''
        This function tests the budget class's regular transfer function. That is, it uses the start transfer date
        and then transfers the amount every frequency until the end transfer date.
        '''

        # Initialize the current date variable
        current_date = transfer.startdate

        # Iterate through each date in the date range
        while current_date <= transfer.enddate:
            # Transfer the amount
            transfer.transfer()

            # Increment the current date by the frequency depending is the frequency is weekly, biweekly, monthly, or yearly
            if transfer.frequency == 'weekly':
                current_date += timedelta(days=7)
            elif transfer.frequency == 'biweekly':
                current_date += timedelta(days=14)
            elif transfer.frequency == 'monthly':
                current_date += timedelta(days=30)
            elif transfer.frequency == 'yearly':
                current_date += timedelta(days=365)

    # Define the total_balance function
    def total_balance(self):
        '''
        This function returns the total balance of the budget object at the end date.
        '''
        # Initialize the total_balance variable
        total_balance = 0

        # Iterate through each account object in the budget object
        for account in self.accounts:
            # Add the account object's balance to the total_balance variable
            total_balance += account.balance

        # Returns the total_balance variable
        return total_balance
    
    # Define the summary_final function
    def summary_final(self):
        '''
        This function returns a string of the budget object's attributes at the end date.
        '''

        account_summary = ''

        # Apply the regular transfers to the account object
        for transfer in self.transfers:
            self.regular_transfer(transfer)

        # Iterate through each account object in the budget object and adjust the balances to account for the money spent and earned and the transfers
        for account in self.accounts:
            total_spent = account.total_bills(self.startdate, self.enddate) + account.total_expenses(self.startdate, self.enddate)
            total_earned = account.total_incomes(self.startdate, self.enddate)
            total_balance = account.balance + total_earned - total_spent

            # Add the account object's summary to the budget_summary string
            account_summary += f'\t{account.name}: ${total_balance:.2f}\n'

        # Creates string for the budget object's attributes
        # "Total spent: ${:.2f}\nTotal earned: ${:.2f}\nTotal balance: ${:.2f}\nAccount balances:\n\t{}: ${:.2f}\n\t{}: ${:.2f}\n".format(expected_total_spent, expected_total_earned, expected_total_balance, account1.name, account1.balance, account2.name, account2.balance)
        budget_summary = f'Total spent: ${self.total_spent():.2f}\nTotal earned: ${self.total_earned():.2f}\nTotal balance: ${self.total_balance()+self.total_earned()-self.total_spent():.2f}\nAccount balances:\n' + account_summary


        # Returns the budget_summary string
        return budget_summary