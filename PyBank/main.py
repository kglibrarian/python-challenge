# Import the os module to create file paths across operating systems
import os

# Import the csv module for reading CSV files
import csv

csvpath = os.path.join('budget_data.csv')

def bankInfo(month, profLoss):
    print("Financial Analysis")
    #print(month)
    monthSum = len(month)
    #print(monthSum)
    print(f"Total Months: {monthSum}" )
    total = 0
    for row in profLoss:
        #print(row)
        total += int(row)
    #print(total)
    print(f"Total: ${total}" )
    average = total / monthSum
    #print(str(round(average,2)))
    print(f"Average Change: ${round(average,2)}" )
    result = list(zip(month, profLoss))
    #print(result)
    maxResult = max(result)
    #print(maxResult)
    print(f"Greatest Increase in Profits: {maxResult[0]} (${maxResult[1]})" )
    minResult = min(result)
    #print(minResult)
    print(f"Greatest Decrease in Profits: {minResult[0]} (${minResult[1]})" )
    #open file and write results to file
    f = open("results.txt", 'w')
    f.write("Financial Analysis\n" f"Total Months: {monthSum}\n" f"Total: ${total}\n" f"Average Change: ${round(average,2)}\n" f"Greatest Increase in Profits: {maxResult[0]} (${maxResult[1]})\n" f"Greatest Decrease in Profits: {minResult[0]} (${minResult[1]})\n")
    f.close()

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    profLoss = []
    month = []
    
    # Read each row of data after the header
    for row in csvreader:
        profLoss.append(row[1])
        month.append(row[0])
    #print(profLoss)
    #print(month)
    

    #* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

    bankInfo(month, profLoss)
    
        
   



