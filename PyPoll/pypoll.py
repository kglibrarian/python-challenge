#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

def voterInfo(voterID, county, candidate):
    #print(voterID)
    
    #The total number of votes cast
    voterSum = len(voterID)
    print(voterSum)
    
    #A complete list of candidates who received votes
    candidateUnique = set(candidate)
    print(candidateUnique)

    #The percentage of votes each candidate won
    #for i in candidate: 
        #my_dict = candidate.count(i) 
        #print(my_dict)
    candidateSum = {i:candidate.count(i) for i in candidate}
    print(candidateSum)

    for i in candidateSum: 
        candidateAvg = ((candidateSum[i]/voterSum)*100)
        print(candidateAvg)
    
    



    #The total number of votes each candidate won
    #The winner of the election based on popular vote.
    result = list(zip(voterID, county, candidate))
    #print(result)
# Import the os module to create file paths across operating systems
import os

# Import the csv module for reading CSV files
import csv

csvpath = os.path.join('election_data_test.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    voterID = []
    county = []
    candidate = []

    # Read each row of data after the header
    for row in csvreader:

        #print(row)
        voterID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        
    #print(profLoss)
    #print(month)
    
    voterInfo(voterID, county, candidate)


  