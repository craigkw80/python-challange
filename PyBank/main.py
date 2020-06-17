# import Modules
import os
import csv


# Setting index 
Month_Count = []
Monthly_Change = []

#Setting some MORE variables and variables for caluclations purposes

Net_PandL = 0
Total_Months = 0
Greatest_Increase = 0
Greatest_Month_Increase = 0
Greatest_Month_Decrease = 0
Greatest_Decrease = 0

 

# Set file path
csvpath = os.path.join('.', 'PyBank', 'Resources', 'budget_data.csv')

# Open csv file as read only and set as variable
with open(csvpath) as csvfile:

# Get Delimiter from csv file.
    csvreader = csv.reader(csvfile, delimiter=',')

# setting some more variables for headers
    header = next(csvreader)
    row = next(csvreader)


    Net_PandL += int(row[1])
    Greatest_Increase = int(row[1])
    Greatest_Month_Increase = row[0]
    past_row = int(row[1])
    Total_Months += 1
    
#Ok lets do some calculations by looping through the Data!!!!!!

    for row in csvreader:

        Net_PandL = int(row[1])
        Total_Months += 1
        
        
        PandL_Change = int(row[1]) - past_row
        Monthly_Change.append(PandL_Change)
        Month_Count.append(row[0])
        past_row = int(row[1])
    

        if int(row[1]) > Greatest_Increase:
            Greatest_Increase = int(row[1])
            Greatest_Month_Increase = row[0]

        if int(row[1]) < Greatest_Increase:
            Greatest_Decrease = int(row[1])
            Greatest_Month_Decrease = row[0]


    High_Change = max(Monthly_Change)
    Low_Change = min(Monthly_Change)
    average = sum(Monthly_Change)/ len(Monthly_Change)

# Show Analysis
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: {Net_PandL}")
print(f"average: ${average:.2f}")
print(f"Greatest Increase in Profits: {Greatest_Month_Increase}, (${High_Change})")
print(f"Greatest Decrease in Profits: {Greatest_Month_Decrease}, (${Low_Change})")

# Export Analysis results to a text file to Analysis folder

output_file = os.path.join('.', 'PyBank', 'Analysis', 'budget_data_revised.text')
with open(output_file, 'w',) as txtfile:

        txtfile.write(f"Financial Analysis\n")
        txtfile.write(f"-------------------------------\n")
        txtfile.write(f"Total Months: {Total_Months}\n")
        txtfile.write(f"Total: ${Net_PandL}\n")
        txtfile.write(f"average: ${average:.2f}\n")
        txtfile.write(f"Greatest Increase in Profits: {Greatest_Month_Increase}, (${High_Change})\n")
        txtfile.write(f"Greatest Decrease in Profits: {Greatest_Month_Decrease}, (${Low_Change})\n")