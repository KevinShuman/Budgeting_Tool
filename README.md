README File

# Project Title
Budgeting Tool

## Description
This is a budgeting tool that allows users to track their personal finances.
The user can add bills, expenses, incomes, bank accounts, and transfers between
accounts, and the tool will calculate the balances within your bank accounts
as well as information about how much you spent and earned for a given amount
of time. There is certainly room to do more with this tool and it is still evolving. 
Feel free to jump on a codespace and play around with it!

There is also a Streamlit-based GUI ([budgeting_app.py](budgeting_app.py)) if you'd
rather build and edit a budget interactively instead of writing a script. See
[Using the GUI](#using-the-gui) below.

## How it works
The library is split into two modules:

* **[budgeting_lib.py](budgeting_lib.py)** defines the core classes: `bill`, `expense`,
  `income`, `account`, `transfer`, and `budget`. Each class models one concept
  (e.g. a `bill` knows its amount, due date, and frequency, and can compute the
  dates it's due between a start and end date). A `budget` ties a set of
  `account` objects and `transfer` objects together over a date range and can
  compute total spent, total earned, and final account balances.
* **[budgeting_other_lib.py](budgeting_other_lib.py)** provides higher-level helpers
  built on top of `budgeting_lib`:
  * `summary_dataframe(...)` takes plain lists/dictionaries describing your
    bills, expenses, incomes, accounts, transfers, and budgets over one or more
    date ranges ("segments") and returns a day-by-day pandas `DataFrame` of
    every account's balance, plus running totals of amount spent and earned.
  * `plot_summary(...)` takes that `DataFrame` and returns a matplotlib figure
    plotting each account's balance over time, with mean/zero reference lines
    and balance labels.

A budget scenario is built from these pieces (see [Plot_Budget.py](Plot_Budget.py)
or [budget_scenario_example.json](budget_scenario_example.json) for concrete examples):

* **`dates`**: a list of `(start_date, end_date)` tuples. Each tuple is a
  "segment" — a continuous period of time with its own bills/expenses/
  incomes/transfers, so you can model changes over time (e.g. a rent increase,
  a new job) without changing the whole scenario. Segments must be contiguous
  (each segment's start date is the day after the previous segment's end date).
* **`bills` / `expenses` / `incomes` / `accounts` / `transfers`**: one list per
  segment, each containing dictionaries describing the individual items for
  that segment (e.g. a bill dictionary has `name`, `amount`, `category`,
  `frequency`, `duedate`, and `ifweekday`).
* **`budgets`**: one dictionary per segment giving that segment's budget a
  `name`.
* **`initial_balances`**: the starting balance of each account, in the same
  order as the first segment's `accounts` list.

Only the account whose `type` is `checking` (case-insensitive) accrues bills,
expenses, and incomes directly; other accounts only change balance through
`transfers` to/from them. This mirrors how the underlying `summary_dataframe`
function is written.

### Class definitions
* **`bill`**: a recurring, due-date-based charge. Attributes: `name`, `amount`,
  `category`, `frequency` (e.g. weekly/monthly/yearly), `startdate`,
  `enddate`, `duedate` (day of the month/period it's due), and `ifweekday`
  (whether it moves to the nearest weekday when the due date falls on a
  weekend).
* **`expense`**: a non-recurring or variable cost tracked for a period.
  Attributes: `name`, `amount`, `category`, and `description`.
* **`income`**: a recurring payment received on a schedule. Attributes:
  `name`, `amount`, `frequency`, `ifweekday`, `category`, `startdate`,
  `enddate`, and `payday` (day of the month/period it's received).
* **`account`**: a bank account that tracks a running `balance` and, for the
  account tied to bills/expenses/incomes, the lists of `bill`, `expense`, and
  `income` objects that affect it. Attributes: `name`, `type` (e.g. checking
  or savings), `balance`, `bills`, `expenses`, `incomes`.
* **`transfer`**: a recurring movement of money between two `account`
  objects. Attributes: `name`, `amount`, `startdate`, `enddate`,
  `depositday`, `frequency`, `from_account`, `to_account`.
* **`budget`**: ties a set of `account` and `transfer` objects together over a
  `startdate`/`enddate` range and computes totals (amount spent, amount
  earned, ending balances per account) for that range. Attributes: `name`,
  `startdate`, `enddate`, `accounts`, `transfers`.

## Getting Started
### Dependencies
* Python 3.11.0
* See [requirements.txt](requirements.txt) for the full list of Python packages
  (pandas, matplotlib, and — if you want the GUI — streamlit are the key ones).

### Installing
* Clone the repository
* You'll want to create a virtual environment to install the dependencies in.
You can do this by running the following command in the root directory of the project:
```
python -m venv <name_you_want_your_env_to_be>
```
* For Linux and Mac OS, activate the virtual environment by running the following
command in the root directory of the project:
```
source <name_you_want_your_env_to_be>/bin/activate
```
* For Windows, activate the virtual environment by running the following command
in the root directory of the project:
```
<name_you_want_your_env_to_be>\Scripts\activate.bat
```
* If for some reason Windows does not allow you to run the activate.bat file, you
can run python commands within the envrionmnet by creating a path to the python.exe
within the environment:
```
\path\to\env\Scripts\python.exe -m pip install -r requirements.txt
```
* Otherwise, once the environment is activated, install the dependencies with:
```
pip install -r requirements.txt
```

### Executing program
* To run the example program, run the following command in the root directory of the project:
```
python Example.py <start date> <end date>
```
* [Plot_Budget.py](Plot_Budget.py) is a ready-to-run scenario script with its dates,
bills, expenses, incomes, accounts, transfers, and initial balances already
hardcoded at the top of the file. Edit those values to match your own budget,
then run it directly — no command-line arguments are needed:
```
python Plot_Budget.py
```
This computes the day-by-day account balances, saves a plot image and a CSV
summary next to the script, and (if run interactively) displays the plot.

### Using the GUI
Instead of editing a Python script, you can build and run a budget scenario
interactively with the Streamlit app in [budgeting_app.py](budgeting_app.py):
```
<path\to\env>\Scripts\python.exe -m streamlit run budgeting_app.py
```
This starts a local web server and opens the app at `http://localhost:8501`.
From there you can:
* Edit the shared **Accounts** table (name, type, and starting balance).
* Add one or more **budget segments** — each is a continuous date range with
  its own editable tables for Bills, Expenses, Incomes, and Transfers.
* Click **Run Budget** to compute the day-by-day summary and plot it, the same
  way [Plot_Budget.py](Plot_Budget.py) does.
* Use **Find a specific day** to look up any single day's account balances
  instead of scrolling the full table.
* Save your work with **Download scenario (JSON)** in the sidebar, and reload
  it later (or share it with someone else) with **Load scenario (JSON)** →
  **Apply loaded scenario**. [budget_scenario_example.json](budget_scenario_example.json) is a
  generic starter scenario you can load to see the expected format.
* Adjust the **Text size (%)** slider in the sidebar to scale the whole app's
  font size up or down.
* Export the resulting day-by-day summary with **Download summary (CSV)**.

## Known caveats and limitations
* **A typo in a transfer's `from_account`/`to_account` name now raises a clear
  `ValueError`** naming the transfer and the unmatched account, instead of
  silently reusing whichever account matched the previous transfer.
* **Segments must be contiguous** (each segment's start date is the day after
  the previous segment's end date). The GUI checks this before running and
  shows an error; scripts that build `dates`/`bills`/etc. directly do not get
  this check and will instead fail with a confusing pandas length-mismatch
  error if segments have a gap or overlap.
* **The GUI's Accounts table is shared across every segment** — you can add
  or remove bills/expenses/incomes/transfers per segment, but not accounts
  themselves; the same set of accounts applies to the whole scenario.
* **Plotting scripts don't call `plt.show()`.** Running one from a plain
  terminal (outside an interactive session) won't pop up a window — it only
  writes the plot image and CSV summary to disk.

### For testing the code
* To run the tests, run the following command in the root directory of the project:
```
pytest
```

## Help
If you have any questions, feel free to reach out to me at kevinshuman17@outlook.com

## Authors
Kevin Shuman




