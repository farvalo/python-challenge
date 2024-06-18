import os
import csv

# Path to the CSV file
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# Initialize variables
total_months = 0
net_total = 0
previous_profit = 0
changes = []
months = []

# Read the CSV file
with open(csvpath, mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        month = row[0]
        profit = int(row[1])
        
        # Calculate total months and net total
        total_months += 1
        net_total += profit
        
        if total_months > 1:
            change = profit - previous_profit
            changes.append(change)
            months.append(month)
        
        previous_profit = profit

# Calculate average change, greatest increase and greatest decrease
average_change = sum(changes) / len(changes)
greatest_increase = max(changes)
greatest_decrease = min(changes)
greatest_increase_month = months[changes.index(greatest_increase)]
greatest_decrease_month = months[changes.index(greatest_decrease)]

# Create analysis report
analysis_report = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)

# Print the analysis to the terminal
print(analysis_report)

# Export the analysis to a text file
output_path = os.path.join('PyBank', 'analysis', 'financial_analysis.txt')

with open(output_path, mode='w') as outputfile:
    outputfile.write(analysis_report)