import os
import csv

# File path
budget_data_csv = os.path.join(r"Resources/budget_data.csv")
output_file = os.path.join(r"Resources", "financial_analysis.txt")

# Variable list
no_of_mo = 0
net_total_profit_and_losses = 0
profit_losses = []
# To calculate the change in profits/losses
previous_profit_loss = None  
# Storing the date for greatest increase and decrease in profits  
dates = []

# Open & read budget_data.csv
with open(budget_data_csv) as csv_file:
    # Read the CSV file
    df = csv.reader(csv_file, delimiter=",")
    # Skip header
    csv_header = next(df)
    
    # Loop through each row after the header
    for row in df:
        # Get the total number of months in the dataset
        no_of_mo += 1
        # Add the current profit/loss to the total
        current_profit_loss = int(row[1])
        net_total_profit_and_losses += current_profit_loss
        #Store dates in a list
        dates.append(row[0])
        # Calculate the difference only if this is not the first row
        if previous_profit_loss is not None:
            difference = current_profit_loss - previous_profit_loss
            profit_losses.append(difference)
        # Update the previous profit/loss for the next iteration
        previous_profit_loss = current_profit_loss

# Calculate statistics
if profit_losses:
    average_of_changes = sum(profit_losses) / len(profit_losses)
    greatest_increase = max(profit_losses)
    greatest_decrease = min(profit_losses)
    greatest_increase_date = dates[profit_losses.index(greatest_increase) + 1]  # +1 for the next month
    greatest_decrease_date = dates[profit_losses.index(greatest_decrease) + 1]

# Print the results
financial_analysis = (
f"Financial Analysis \n\n"
f"---------------------------- \n\n"
f"Total Months: {no_of_mo} \n\n"
f"Total: ${net_total_profit_and_losses:.2f} \n\n"
f"Average Change: ${average_of_changes:.2f} \n\n"
f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase}) \n\n"
f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease}) \n\n"
)
print(financial_analysis)

# Write results to a text file
with open(output_file, 'w') as file:
    file.write(financial_analysis)

