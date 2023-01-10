# Import modulesfor the analysis
import os
import csv
# Path for csv file

data_path=os.path.join('Resources', 'budget_data.csv')

# Count total number of months
total_months = 0

# Count total profit and loss
total_profit_loss = 0

# Count output value of total profit and loss
value = 0

# Count output value of total profit and loss
change = 0

# List to hold the dates of the financial records
dates = []

# List to hold the profits/loss
profits = []

# Read csv file
with open(data_path, newline="") as budget_file:
    csvreader = csv.reader(budget_file, delimiter=",")
    # Reading header row
    csv_header = next(csvreader)
    # Go to the first row


    first_row = next(csvreader)

    # Add total month count

    total_months += 1

    # Add profit and loss count

    total_profit_loss += int(first_row[1])
    value = int(first_row[1])
    # Read the rows after the header row
    for row in csvreader:

        # Get the date
        dates.append(row[0])

        # Keep the the records of changes in rows
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])

        # Total number of months
        total_months += 1

        # Net total amount of profit/ losses over the entire period

        total_profit_loss = total_profit_loss + int(row[1])

        # Average of the changes in "Profit/Losses" over the entire period

        avg_change = sum(profits)/len(profits)
  # The greatest increase in profits
    greatest_increase = max(profits)
    greatest_inc_index = profits.index(greatest_increase)
    greatest__inc_date = dates[greatest_inc_index]

    # The greatest decrease in profits
    greatest_decrease = min(profits)
    greatest__dec_index = profits.index(greatest_decrease)
    greatest__dec_date = dates[greatest__dec_index]

#Printing the analysis output
printoutput = (
    f"Financial Analysis\n"
    f"-------------------------------------\n"
    f"Total Months: {str(total_months)}\n"
    f"Total: ${str(total_profit_loss)}\n"
    f"Average Change: ${str(round(avg_change,2))}\n"
    f"Greatest Increase in Profits: {greatest__inc_date} (${str(greatest_increase)})\n"
    f"Greatest Decrease in Profits: {greatest__dec_date} (${str(greatest_decrease)})\n")
print(printoutput)

# Exporting to text file

output_file = os.path.join('Analysis', 'PyBank_Analysis.txt')


PyBank_Analysis = open(output_file, "w")

line1 = "Financial Analysis"
line2 = "------------------------------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_profit_loss)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(
    f"Greatest Increase in Profits: {greatest__inc_date} (${str(greatest_increase)})")
line7 = str(
    f"Greatest Decrease in Profits: {greatest__dec_date} (${str(greatest_decrease)})")
PyBank_Analysis.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(
    line1, line2, line3, line4, line5, line6, line7))


# This code is written for Module Challenge Three of the Data Analytics Bootcamp taught through Rice University