import json
from collections import defaultdict
from dateutil.parser import parse

# Load the data from the JSON file
with open('transactions.json', 'r') as f:
    data = json.load(f)

# Initialize revenue and expenses
monthly_summary = defaultdict(lambda: {'revenue': 0, 'expenses': 0})

# Iterate over the data
for item in data:
    # Extract the month from the date
    date = parse(item['created_at'])
    month = date.strftime('%m')  # Format the date as 'MM'

    # Check if the number is positive or negative
    if item['amount'] >= 0:
        monthly_summary[month]['revenue'] += item['amount']
    else:
        monthly_summary[month]['expenses'] += abs(item['amount'])  # Convert to positive before adding

# Print the monthly summary
for month in sorted(monthly_summary.keys()):
    summary = monthly_summary[month]
    revenue = "{:,} Kip".format(summary['revenue'])
    expenses = "{:,} Kip".format(summary['expenses'])
    print(f'Month: {month}: \n Total Revenue: {revenue} \n Total Expenses: {expenses}')
