# import Modules
import os
import csv

total_votes = 0
canidates = 0
Correy =0
Khan = 0
Li = 0
Otooley = 0

# Set Path For File
csvpath = os.path.join('.', 'PyPoll', 'Resources', 'election_data.csv')

# Open & Read CSV File
with open(csvpath) as csvfile:

    #specify delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read header first
    csv_header = next(csvfile)

    # Read all rows of data except header
    for row in csvreader:
        
        # Calculate Total number of votes
        total_votes += 1
        
        # Calculate Total number of votes for everyone
        if (row[2] == "Khan"):
            Khan += 1
        elif (row[2] == "Correy"):
            Correy += 1
        elif (row[2] == "Li"):
            Li += 1
        else:
            Otooley += 1
            
    # Calculate Percentage Of Votes Each Candidate Won
    kahn_percent = Khan / total_votes
    correy_percent = Correy / total_votes
    li_percent = Li / total_votes
    otooley_percent = Otooley / total_votes
    
    # Calculate Winner Of The Election Based On Popular Vote
    winner = max(Khan, Correy, Li, Otooley)

    if winner == Khan:
        winner_is = "Khan"
    elif winner == Correy:
        winner_is = "Correy"
    elif winner == Li:
        winner_is = "Li"
    else:
        winner = "O'Tooley" 


print("Elcection Results\n")
print("------------------------------\n")
print(f"Total Votes: {total_votes}\n")
print("------------------------------\n")
print(f"Kahn: {kahn_percent:.3%}({Khan})")
print(f"Correy: {correy_percent:.3%}({Correy})")
print(f"Li: {li_percent:.3%}({Li})")
print(f"O'Tooley: {otooley_percent:.3%}({Otooley})\n")
print("------------------------------\n")
print(f"Winner: {winner_is}\n")
print("------------------------------\n")


# Export Analysis results to a text file to Analysis folder

output_file = os.path.join('.', 'PyPoll', 'Analysis', 'election_data_revised.text')
with open(output_file, 'w',) as txtfile:

        txtfile.write("Elcection Results\n")
        txtfile.write("------------------------------\n")
        txtfile.write(f"Total Votes: {total_votes}\n")
        txtfile.write("------------------------------\n")
        txtfile.write(f"Kahn: {kahn_percent:.3%}({Khan})\n")
        txtfile.write(f"Correy: {correy_percent:.3%}({Correy})\n")
        txtfile.write(f"Li: {li_percent:.3%}({Li})\n")
        txtfile.write(f"O'Tooley: {otooley_percent:.3%}({Otooley})\n")
        txtfile.write("------------------------------\n")
        txtfile.write(f"Winner: {winner_is}\n")
        txtfile.write("------------------------------\n")