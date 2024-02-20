import json

# Load the data from the JSON file
with open('transactions.json', 'r') as f:
    data = json.load(f)

# Initialize revenue and expenses
total_revenue = 0
total_expenses = 0

# Iterate over the data
for item in data:
    # Check if the number is positive or negative
    if item['amount'] >= 0:
        total_revenue += item['amount']
    else:
        total_expenses += abs(item['amount'])  # Convert to positive before adding

# Format the numbers with commas
total_revenue = "{:,} Kip".format(total_revenue)
total_expenses = "{:,} Kip".format(total_expenses)

print(f'Total Revenue: {total_revenue}')
print(f'Total Expenses: {total_expenses}')
