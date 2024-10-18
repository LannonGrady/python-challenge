# -*- coding: UTF-8 -*-

import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("C:/Users/lanno/Dropbox/PC/Desktop/Data Analytics Class/python-challenge/PyPoll/Resources/election_data.csv")  # Input file path
file_to_output = os.path.join("C:/Users/lanno/Dropbox/PC/Desktop/Data Analytics Class/python-challenge/PyPoll/analysis/election_analysis.txt")  # Output file path

# Define variables to track the polling data
total_votes = 0
max_votes = 0
politicians = {}

with open(file_to_load, 'r') as election_data:
    reader = csv.reader(election_data, delimiter=",")
        
    # Skip the header row
    header = next(reader)
    
    # Count total votes and establish which CSV column contains needed data
    for row in reader:
        total_votes += 1
        candidate = row[2] 

        # Create dictionary of unique candidates and count votes for each candidate
        if candidate in politicians:
            politicians[candidate] += 1

        else:
            politicians[candidate] = 1

# Print part I of the required output format and total votes
print("Election Results")
print("-------------------------")
print(f'Total Votes: {total_votes:,}')
print("-------------------------")

# Write the same results and formatting to a text file
with open(file_to_output, "a") as txt_file:
    
    txt_file.write("Election Results \n\n")
    txt_file.write("-------------------------\n\n")
    txt_file.write(f'Total Votes: {total_votes:,}\n\n')
    txt_file.write("-------------------------\n\n")

# Create a loop to find the winner and print out percentage of votes received in desired format
for names,votes in politicians.items():
            
        percent = (votes / total_votes) * 100

        if votes > max_votes:
            max_votes = votes
            winner = names
        else:
            max_votes = max_votes
        print(f'{names}: {percent:.03F}% ({votes:,})')
        with open(file_to_output, "a") as txt_file:
            txt_file.write(f'{names}: {percent:.03F}% ({votes:,})\n\n')

# Print part II of the required formatting announcing winner 
print("-------------------------")
print(f'Winner: {winner}')
print("-------------------------")

# Continue writing part II of the results to the text file 
with open(file_to_output, "a") as txt_file:
    txt_file.write("-------------------------\n\n")
    txt_file.write(f'Winner: {winner}\n\n')
    txt_file.write("-------------------------")
