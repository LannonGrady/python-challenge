# -*- coding: UTF-8 -*-

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("C:/Users/lanno/Dropbox/PC/Desktop/Data Analytics Class/python-challenge/PyBank/Resources/budget_data.csv")  # Input file path
file_to_output = os.path.join("C:/Users/lanno/Dropbox/PC/Desktop/Data Analytics Class/python-challenge/PyBank/analysis/budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
start_month = 0
end_month = 0

# Add more variables to track other necessary financial data
max_profit = 0
min_profit = 0

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=",")

    # Extract first row to avoid appending to net_change_list
    for row_index, row in enumerate(reader):
        if row_index == 1:
            start_month = int(row[1])
            break
    financial_data.seek(0)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:
          
        # Track the total and net change
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        end_month = int(row[1])

        # Calculate the greatest increase in profits (month and amount)
        if int(row[1]) > max_profit:
            max_profit = int(row[1])
            max_month = str(row[0])
        elif int(row[1]) < min_profit:
            min_profit = int(row[1])
            min_month = str(row[0])

# Calculate the average net change across the months
avg_monthly_chg = (end_month - start_month)/(total_months-1)

# Print the output
def screen_output(): 
    print("Financial Analysis \n----------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total Profit Over Time: ${total_net:,.0f}')
    print(f'Average Change: ${avg_monthly_chg:,.2f}')
    print(f'Greatest Increase in Profits: {max_month}, ${max_profit:,.0f}')
    print(f'Greatest Decrease in Profits: {min_month}, ${min_profit:,.0f}')

screen_output()

# Write the results to a text file

def file_output(): 
    
    with open(file_to_output, "w") as txt_file:
    
        txt_file.write("Financial Analysis \n\n")
        txt_file.write("----------------------------\n\n")
        txt_file.write(f'Total Months: {total_months}\n\n')
        txt_file.write(f'Total Profit Over Time: ${total_net:,.0f}\n\n')
        txt_file.write(f'Average Change: ${avg_monthly_chg:,.2f}\n\n')
        txt_file.write(f'Greatest Increase in Profits: {max_month}, ${max_profit:,.0f}\n\n')
        txt_file.write(f'Greatest Decrease in Profits: {min_month}, ${min_profit:,.0f}\n\n')

file_output()