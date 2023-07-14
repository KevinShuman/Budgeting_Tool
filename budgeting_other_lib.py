import budgeting_lib as bl
import datetime as dt
import pandas as pd

# Define a function that takes in a list of dates; lists of lists of bills, expenses, incomes, accounts, and transfers;
# a list of budget objects; and creates a pandas dataframe of the budget objects' summaries
def summary_dataframe(dates, bills, expenses, incomes, accounts, transfers, budgets, initial_balances):
    '''
    This function returns a pandas dataframe of the budget objects' summaries.

    Inputs:
        dates (list): The list of dates over the range of considered dates. This divides up
                        the bills, expenses, incomes, transfers, and accounts into the different
                        budget objects to handle changes in those objects over time.
        bills (list): The list of lists of bill objects over the range of considered dates.
        expenses (list): The list of lists of expense objects over the range of considered dates.
        incomes (list): The list of lists of income objects over the range of considered dates.
        accounts (list): The list of lists of account objects over the range of considered dates.
        transfers (list): The list of lists of transfer objects over the range of considered dates.
        budgets (list): The list of budget objects over the range of considered dates.
        initial_balances (list): The list of initial balances of the accounts at the very start.

    Returns:
        budget_summary (dataframe): The dataframe of the budget objects' for each date in the date range.   
    '''
    
    # Initialize the budget_summary dataframe
    budget_summary = pd.DataFrame()

    # Initialize the budget_summary_outputs list
    budget_summary_outputs = []

    counter = 0
    # Pull the pairs of dates from the dates list. Every pair of dates is a start date and an end date.
    for date, budget_dict, bill_list, expense_list, income_list, transfer_list, account_list in zip(dates, budgets, bills, expenses, incomes, transfers, accounts):
        startdate = date[0]
        enddate = date[1]

        dates_between = []
        for i in range((enddate - startdate).days + 1):     
            dates_between.append(startdate + dt.timedelta(i))

        for i, date in enumerate(dates_between):
            # Create the bills list for the budget object
            # The parameter is a list of list of dictionaries, so the shape looks like [[{bill1}, {bill2}, ...], [{bill1}, {bill2}, ...], ...]
            # The dictionaries have the following keys: name, amount, category, frequency, duedate, and ifweekday. These are
            # the attributes of the bill object that are used to create the bill object in additon to the startdate and enddate.
            # We need to create a list of bills for each date in the date range using the dictionary information.
            bills_list = []
            for bill_dict in bill_list:
                bills_list.append(bl.bill(name=bill_dict['name'], amount=bill_dict['amount'], category=bill_dict['category'], frequency=bill_dict['frequency'], duedate=bill_dict['duedate'], ifweekday=bill_dict['ifweekday'], startdate=startdate, enddate=date))

            # Create the expenses list for the budget object
            # The parameter is a list of list of dictionaries, so the shape looks like [[{expense1}, {expense2}, ...], [{expense1}, {expense2}, ...], ...]
            # The dictionaries have the following keys: name, amount, category, description
            # We need to create a list of expenses for each date in the date range using the dictionary information.
            expenses_list = []
            for expense_dict in expense_list:
                expenses_list.append(bl.expense(name=expense_dict['name'], amount=expense_dict['amount'], category=expense_dict['category'], description=expense_dict['description']))

            # Create the incomes list for the budget object
            # The parameter is a list of list of dictionaries, so the shape looks like [[{income1}, {income2}, ...], [{income1}, {income2}, ...], ...]
            # The dictionaries have the following keys: name, amount, payday, ifweekday, category, frequency
            # We need to create a list of incomes for each date in the date range using the dictionary information.
            incomes_list = []
            for income_dict in income_list:
                incomes_list.append(bl.income(name=income_dict['name'], amount=income_dict['amount'], payday=income_dict['payday'], ifweekday=income_dict['ifweekday'], category=income_dict['category'], startdate=startdate, enddate=date, frequency=income_dict['frequency']))

            # Create the accounts list for the budget object
            # The parameter is a list of list of dictionaries, so the shape looks like [[{account1}, {account2}, ...], [{account1}, {account2}, ...], ...]
            # The dictionaries have the following keys: name, type
            # We need to create a list of accounts for each date in the date range using the dictionary information.
            accounts_list = []
            for j, account_dict in enumerate(account_list):
                if counter == 0:
                    # Check if the account is called "Checking"
                    if account_dict['name'] == 'Checking':
                        name = account_dict['name']
                        # print(f'{name}: {j} {counter} {date}')
                        accounts_list.append(bl.account(name=account_dict['name'], type=account_dict['type'], balance=initial_balances[j], bills=bills_list, expenses=expenses_list, incomes=incomes_list))
                    else:
                        # name = account_dict['name']
                        # print(f'{name}: {j} {counter} {date}')
                        accounts_list.append(bl.account(name=account_dict['name'], type=account_dict['type'], balance=initial_balances[j], bills=[], expenses=[], incomes=[]))
                else:
                    if account_dict['name'] == 'Checking':
                        name = account_dict['name']
                        # print(f'{name}: {j} {counter} {date}')
                        accounts_list.append(bl.account(name=account_dict['name'], type=account_dict['type'], balance=final_balances[j+3], bills=bills_list, expenses=expenses_list, incomes=incomes_list))
                    else:
                        # name = account_dict['name']
                        # print(f'{name}: {j} {counter} {date}')
                        accounts_list.append(bl.account(name=account_dict['name'], type=account_dict['type'], balance=final_balances[j+3], bills=[], expenses=[], incomes=[]))

            # Create the transfers list for the budget object
            # The parameter is a list of list of dictionaries, so the shape looks like [[{transfer1}, {transfer2}, ...], [{transfer1}, {transfer2}, ...], ...]
            # The dictionaries have the following keys: name, amount, from_account, to_account, frequency, depositday
            # We need to create a list of transfers for each date in the date range using the dictionary information.
            transfers_list = []
            for transfer_dict in transfer_list:
                # Find what from_account and to_account are in the accounts_list using the names in the transfer_dict
                for account in accounts_list:
                    if account.name == transfer_dict['from_account'].lower():
                        from_account = account
                    if account.name == transfer_dict['to_account'].lower():
                        to_account = account
                transfers_list.append(bl.transfer(name=transfer_dict['name'], amount=transfer_dict['amount'], from_account=from_account, to_account=to_account, frequency=transfer_dict['frequency'], depositday=transfer_dict['depositday'], startdate=startdate, enddate=date))

            # Create the budget object
            # The parameter is a list of dictionaries, so the shape looks like [{budget1}, {budget2}, ...]
            # The dictionaries have the following keys: name, accounts, transfers, startdate, enddate
            # We need to create a budget object for each date in the date range using the dictionary information.
            budget_thing = bl.budget(name=budget_dict['name'], accounts=accounts_list, transfers=transfers_list, startdate=startdate, enddate=date)

            # Create the budget summary dataframe for the budget object
            budget_summary_outputs.append(budget_thing.summary_final(dict=True))

            # If the counter is greater than 0, then we need to add the total spent, 
            # total earned, and total balance from the last date to each of the
            # next set of dates

            if counter > 0:
                addition_spent = total_spent + budget_summary_outputs[-1]['Total Spent']
                addition_earned = total_earned + budget_summary_outputs[-1]['Total Earned']

                budget_summary_outputs[-1]['Total Spent'] = addition_spent
                budget_summary_outputs[-1]['Total Earned'] = addition_earned

            # If the date is the last date in the date range, then we need to find the final balances of the accounts
            if date == dates_between[-1]:
                total_spent = budget_summary_outputs[-1]['Total Spent']
                total_earned = budget_summary_outputs[-1]['Total Earned']
                total_balance = budget_summary_outputs[-1]['Total Balance']
                final_balances = [total_spent, total_earned, total_balance]
                for account in accounts_list:
                    final_balances.append(budget_summary_outputs[-1][account.name.lower() + ' Balance'])

        counter += 1

    # Create a list of all the dates between the startdate and enddate from the first tuple in the dates list
    # to the last tuple in the dates list
    dates_between = []
    for i in range((dates[-1][-1] - dates[0][0]).days + 1):
        dates_between.append(dates[0][0] + dt.timedelta(i))

    # Create the budget summary dataframe
    budget_summary = pd.DataFrame(budget_summary_outputs, index=dates_between)

    # Remove the Total Spent, Total Income, and Total Balance columns
    # budget_summary = budget_summary.drop(columns=['Total Spent', 'Total Earned', 'Total Balance'])

    return budget_summary

