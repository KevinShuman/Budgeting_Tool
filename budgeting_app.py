'''
Budget Builder - a Streamlit GUI for budgeting_lib / budgeting_other_lib.

What it does:
    Lets you define one or more continuous "budget segments" (time periods),
    each with its own bills, expenses, incomes, and transfers, plus a shared
    set of accounts and starting balances. Running the budget calls
    bol.summary_dataframe(...) and plots the account balances over time with
    bol.plot_summary(...), the same functions used by the My_Budget_*.py
    scripts. Scenarios can be saved/loaded as JSON and results exported as CSV.

How to run it:
    From the project root, with the virtual environment's Python:
        budgetingenv\\Scripts\\python.exe -m streamlit run budgeting_app.py
    This opens the app in a browser tab at http://localhost:8501.

Note:
    Only the account whose type is "checking" tracks bills/expenses/incomes;
    this mirrors budgeting_other_lib.summary_dataframe.
'''

import streamlit as st
import pandas as pd
import datetime as dt
import json

import budgeting_other_lib as bol

st.set_page_config(page_title="Budget Builder", layout="wide")

if 'text_scale' not in st.session_state:
    st.session_state.text_scale = 100

with st.sidebar:
    st.header("Display")
    st.session_state.text_scale = st.slider("Text size (%)", min_value=70, max_value=200, value=st.session_state.text_scale, step=10)

# Scales the app's base font size; most Streamlit text/table/widget sizes are
# defined in rem units, so this rescales nearly everything at once
st.markdown(f"<style>html {{ font-size: {st.session_state.text_scale}%; }}</style>", unsafe_allow_html=True)

st.title("Budget Builder")

FREQUENCIES = ['Weekly', 'Biweekly', 'Monthly', 'Yearly']
ACCOUNT_TYPES = ['checking', 'savings']

DEFAULT_BILL = {'name': '', 'amount': 0.0, 'category': 'Subscription', 'frequency': 'Monthly', 'duedate': 1, 'ifweekday': False}
DEFAULT_EXPENSE = {'name': '', 'amount': 0.0, 'category': 'Expense', 'description': ''}
DEFAULT_INCOME = {'name': '', 'amount': 0.0, 'payday': 1, 'ifweekday': False, 'category': 'Income', 'frequency': 'Biweekly'}
DEFAULT_TRANSFER = {'name': '', 'amount': 0.0, 'from_account': 'Checking', 'to_account': 'Savings', 'frequency': 'biweekly', 'depositday': 1}


def init_state():
    if 'data_version' not in st.session_state:
        st.session_state.data_version = 0
    if 'accounts' not in st.session_state:
        st.session_state.accounts = [
            {'name': 'Checking', 'type': 'checking', 'initial_balance': 0.0},
            {'name': 'Savings', 'type': 'savings', 'initial_balance': 0.0},
        ]
    if 'segments' not in st.session_state:
        st.session_state.segments = [{
            'budget_name': 'budget1',
            'start': dt.date.today(),
            'end': dt.date.today() + dt.timedelta(days=30),
            'bills': [DEFAULT_BILL.copy()],
            'expenses': [DEFAULT_EXPENSE.copy()],
            'incomes': [DEFAULT_INCOME.copy()],
            'transfers': [DEFAULT_TRANSFER.copy()],
        }]


init_state()

# --- Save / Load scenario ---
with st.sidebar:
    st.header("Scenario file")

    def scenario_to_json():
        data = {
            'accounts': st.session_state.accounts,
            'segments': [
                {**seg, 'start': seg['start'].isoformat(), 'end': seg['end'].isoformat()}
                for seg in st.session_state.segments
            ],
        }
        return json.dumps(data, indent=2)

    st.download_button("Download scenario (JSON)", scenario_to_json(), file_name="budget_scenario.json")

    uploaded = st.file_uploader("Load scenario (JSON)", type="json")
    if uploaded is not None and st.button("Apply loaded scenario"):
        data = json.load(uploaded)
        data['segments'] = [
            {**seg, 'start': dt.date.fromisoformat(seg['start']), 'end': dt.date.fromisoformat(seg['end'])}
            for seg in data['segments']
        ]
        st.session_state.accounts = data['accounts']
        st.session_state.segments = data['segments']
        st.session_state.data_version += 1
        st.rerun()

# --- Accounts (shared across all segments) ---
st.header("Accounts")
st.caption("Accounts and their starting balances apply across every budget segment below. Only the account with type 'checking' tracks bills/expenses/incomes; other accounts only move money via transfers.")

accounts_df = pd.DataFrame(st.session_state.accounts)
accounts_df = st.data_editor(
    accounts_df,
    num_rows="dynamic",
    column_config={
        "type": st.column_config.SelectboxColumn(options=ACCOUNT_TYPES),
        "initial_balance": st.column_config.NumberColumn(format="$%.2f"),
    },
    key=f"accounts_editor_v{st.session_state.data_version}",
)
st.session_state.accounts = accounts_df.to_dict("records")

account_names = [a['name'] for a in st.session_state.accounts if a.get('name')]

st.divider()

# --- Segments ---
st.header("Budget segments")
st.caption("Each segment is a continuous time period with its own bills, expenses, incomes, and transfers.")

col_add, col_remove = st.columns(2)
if col_add.button("Add segment"):
    last = st.session_state.segments[-1]
    st.session_state.segments.append({
        'budget_name': f'budget{len(st.session_state.segments) + 1}',
        'start': last['end'] + dt.timedelta(days=1),
        'end': last['end'] + dt.timedelta(days=30),
        'bills': [row.copy() for row in last['bills']],
        'expenses': [row.copy() for row in last['expenses']],
        'incomes': [row.copy() for row in last['incomes']],
        'transfers': [row.copy() for row in last['transfers']],
    })
    st.session_state.data_version += 1
    st.rerun()
if col_remove.button("Remove last segment") and len(st.session_state.segments) > 1:
    st.session_state.segments.pop()
    st.session_state.data_version += 1
    st.rerun()

for i, seg in enumerate(st.session_state.segments):
    with st.expander(f"Segment {i + 1}: {seg['budget_name']} ({seg['start']} to {seg['end']})", expanded=(i == len(st.session_state.segments) - 1)):
        v = st.session_state.data_version
        name_col, start_col, end_col = st.columns(3)
        seg['budget_name'] = name_col.text_input("Budget name", value=seg['budget_name'], key=f"name_{i}_v{v}")
        seg['start'] = start_col.date_input("Start date", value=seg['start'], key=f"start_{i}_v{v}")
        seg['end'] = end_col.date_input("End date", value=seg['end'], key=f"end_{i}_v{v}")

        st.subheader("Bills")
        bills_df = st.data_editor(
            pd.DataFrame(seg['bills']),
            num_rows="dynamic",
            column_config={
                "frequency": st.column_config.SelectboxColumn(options=FREQUENCIES),
                "duedate": st.column_config.NumberColumn(min_value=1, max_value=31, step=1),
                "amount": st.column_config.NumberColumn(format="$%.2f"),
            },
            key=f"bills_{i}_v{v}",
        )
        seg['bills'] = bills_df.to_dict("records")

        st.subheader("Expenses")
        expenses_df = st.data_editor(
            pd.DataFrame(seg['expenses']),
            num_rows="dynamic",
            column_config={"amount": st.column_config.NumberColumn(format="$%.2f")},
            key=f"expenses_{i}_v{v}",
        )
        seg['expenses'] = expenses_df.to_dict("records")

        st.subheader("Incomes")
        incomes_df = st.data_editor(
            pd.DataFrame(seg['incomes']),
            num_rows="dynamic",
            column_config={
                "frequency": st.column_config.SelectboxColumn(options=FREQUENCIES),
                "payday": st.column_config.NumberColumn(min_value=1, max_value=31, step=1),
                "amount": st.column_config.NumberColumn(format="$%.2f"),
            },
            key=f"incomes_{i}_v{v}",
        )
        seg['incomes'] = incomes_df.to_dict("records")

        st.subheader("Transfers")
        transfers_df = st.data_editor(
            pd.DataFrame(seg['transfers']),
            num_rows="dynamic",
            column_config={
                "from_account": st.column_config.SelectboxColumn(options=account_names),
                "to_account": st.column_config.SelectboxColumn(options=account_names),
                "depositday": st.column_config.NumberColumn(min_value=1, max_value=31, step=1),
                "amount": st.column_config.NumberColumn(format="$%.2f"),
            },
            key=f"transfers_{i}_v{v}",
        )
        seg['transfers'] = transfers_df.to_dict("records")

st.divider()

# --- Run the budget ---
if st.button("Run Budget", type="primary"):
    # Segments must be contiguous (each start = previous end + 1 day) or the
    # resulting summary_dataframe row count won't match its date index
    gaps = [
        (i, prev['end'], seg['start'])
        for i, (prev, seg) in enumerate(zip(st.session_state.segments, st.session_state.segments[1:]), start=1)
        if seg['start'] != prev['end'] + dt.timedelta(days=1)
    ]
    if gaps:
        for i, prev_end, next_start in gaps:
            st.error(f"Segment {i + 1} starts {next_start}, but segment {i} ends {prev_end}. Segments must be contiguous (no gaps or overlaps).")
    else:
        try:
            dates = [(seg['start'], seg['end']) for seg in st.session_state.segments]
            account_list = [{'name': a['name'], 'type': a['type']} for a in st.session_state.accounts]
            accounts = [account_list for _ in st.session_state.segments]
            bills = [seg['bills'] for seg in st.session_state.segments]
            expenses = [seg['expenses'] for seg in st.session_state.segments]
            incomes = [seg['incomes'] for seg in st.session_state.segments]
            transfers = [seg['transfers'] for seg in st.session_state.segments]
            budgets = [{'name': seg['budget_name']} for seg in st.session_state.segments]
            initial_balances = [a['initial_balance'] for a in st.session_state.accounts]

            summary = bol.summary_dataframe(dates, bills, expenses, incomes, accounts, transfers, budgets, initial_balances)
            summary = summary.drop(columns=['Total Spent', 'Total Earned', 'Total Balance'])

            st.session_state['last_summary'] = summary
        except Exception as e:
            st.error(f"Could not run budget: {e}")

if 'last_summary' in st.session_state:
    summary = st.session_state['last_summary']
    fig = bol.plot_summary(summary)
    st.pyplot(fig)

    st.download_button("Download summary (CSV)", summary.to_csv(), file_name="budget_summary.csv")

    st.subheader("Find a specific day")
    min_date, max_date = summary.index.min(), summary.index.max()
    search_date = st.date_input("Date", value=min_date, min_value=min_date, max_value=max_date, key="search_date")
    if search_date in summary.index:
        st.dataframe(summary.loc[[search_date]])
    else:
        st.warning(f"{search_date} is outside the budget's date range ({min_date} to {max_date}).")

    st.dataframe(summary)
