# Import the os module to create file paths across operating systems
import os

# Import the csv module for reading CSV files
import csv

csvpath = os.path.join('budget_data.csv')

def bankInfo(bankData):
           
        #these work: 
        #print(bankData[1])
        profLoss = (bankData[1])
        date = (bankData[0])
        
        print(date)
        print(profLoss)
    
    #for number in bankData:
        #print(bankData)

        #totalMonths += number
        #return totalMonths
        #print(totalMonths)
    
    
    #totalMonths = sum(bankData[1])

    #this works:
    #print(bankData[1])
  
    
    #print(months)

    # The net total amount of "Profit/Losses" over the entire period
    #for number in bankData:
        #total += number
       #return total
    #AmtProfLoss = sum(int(bankData(2)))
    #print(AmtProfLoss)

    # The average of the changes in "Profit/Losses" over the entire period
    #AvgAmtProfLoss = AmtProfLoss/monthsLen
    #print(AvgAmtProfLoss)

    # The greatest increase in profits (date and amount) over the entire period
    #MaxAmtProfLoss = max(bankData(2))
    #print(MaxAmtProfLoss)

    # The greatest decrease in losses (date and amount) over the entire period
    #MinAmtProfLoss = min(bankData(2))
    #print(MinAmtProfLoss)
    
# Write a function that returns the arithmetic average for a list of numbers
#def average(numbers):
    #length = len(numbers)
    #total = 0.0
    #for number in numbers:
        #total += number
    #return total / length

# Test your function with the following:
#print(average([1, 5, 9]))
#print(average(range(11)))







with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
 
    # Read each row of data after the header
    for row in csvreader:
        #print(int(row[1]))

        # If the wrestler's name in a row is equal to that which the user input, run the 'getPercentages()' function
        #if(nameToCheck == row[0]):
            #getPercentages(row)
        bankInfo(row)

# The total number of months included in the dataset
#* The net total amount of "Profit/Losses" over the entire period
#* The average of the changes in "Profit/Losses" over the entire period
#* The greatest increase in profits (date and amount) over the entire period
#* The greatest decrease in losses (date and amount) over the entire period

