# The total number of months included in the dataset
#* The net total amount of "Profit/Losses" over the entire period
#* The average of the changes in "Profit/Losses" over the entire period
#* The greatest increase in profits (date and amount) over the entire period
#* The greatest decrease in losses (date and amount) over the entire period

# Import the os module to create file paths across operating systems
import os

# Import the csv module for reading CSV files
import csv




csvpath = os.path.join('budget_data.csv')

# The total number of months included in the dataset
def monthTotal(month):
    monthSum = len(month)
    #print(monthSum)

# The net total amount of "Profit/Losses" over the entire period
def profLossSum(profLoss):
    #print(profLoss)
    total = 0
    for row in profLoss:
        #print(row)
        total += int(row)
    #print(total)
    return(total)
    

# The average of the changes in "Profit/Losses" over the entire period
def profLossAvg(total):
    print(total)

#def bankInfo(bankData):
        
        #these work: 
        #print(bankData[1])
        #profLoss = []
        #row = bankData[1]
        #print(row)
    


        

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    profLoss = []
    month = []
    #total = 0
    
    # Read each row of data after the header
    for row in csvreader:
        profLoss.append(row[1])
        month.append(row[0])
    #print(profLoss)
    #print(month)
    monthTotal(month)
    profLossSum(profLoss)
    #profLossAvg(total)
    
        
   



