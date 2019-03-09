# Import the os module to create file paths across operating systems
import os

# Import the csv module for reading CSV files
import csv

csvpath = os.path.join('election_data_test.csv')

#```text
  #Election Results
  #-------------------------
  #Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
 # -------------------------
  #```

#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

def voterInfo(voterID, county, candidate):
        
    #The total number of votes cast
    voterSum = len(voterID)
    print(f"Total Votes: {voterSum}")
   
    #A complete list of candidates who received votes
    #candidateUnique = set(candidate)
    #print(candidateUnique)

    #Create dicitonary of Key: candidate name and Value: number of votes
    candidateSum = {i:candidate.count(i) for i in candidate}
    
    #print("candidateSum: ", candidateSum)
    for i in candidateSum:
        print(i)
    
    #candidatePercent = []

    #create an empty dictionary for the final data
    finalData = {}

    #loop through each Key: candidate in our current dictionary
    for k, v in candidateSum.items():
        if v < 
        #print(k, v[0], v[1])
        print(f"{k} : {v[0]} ({v[1]})")
        
        #each Key: candidate should be i
        #print("i: ", i)
        
        #sum the number of unique times each candidate was voted for
        candidateVoteSum = len(i)
        #print("CandidateVoteSum: ", candidateVoteSum)
        
        #get the average number of votes each candidate received - create a percentage and round to two decimals
        candidateAvg = (candidateSum[i]/voterSum)*100
        candidateAvgRound = round(candidateAvg,3)
        #print("CandidateAvgRound: ",  candidateAvgRound)

        #create a list of the data for each candidate - which is the average number of votes received, and the number of votes
        candidateInfo = {i:[candidateAvgRound, candidateVoteSum]}
        #print("CandidateInfo: ", candidateInfo)
        
        #add this new informaiton into our dictionary
        finalData.update(candidateInfo)
    
    #print the finalData dictionary
    #print(finalData)
    
    #loop through the items in the dictionary and print them
    for k, v in finalData.items():
        #print(k, v[0], v[1])
        print(f"{k} : {v[0]} ({v[1]})")
           
    #print(finalData(1))
        #candidatePercent.append(candidateInfo)
    #print(candidatePercent)
    #print(candidatePercent.iteritems())
    
    #delete from function here down!!

    #print(f"{candidatePercent[0]} \n" f"{candidatePercent[1]}")
    #print(f"Average Change: ${round(average,2)}" )

        #candidatePercent.append({i:candidateAvg})
      
    
    #result = list(zip(candidateUnique, candidateAvg))
    #print(result)


    #The total number of votes each candidate won
    #The winner of the election based on popular vote.
    #result = list(zip(voterID, county, candidate))
    #print(result)




with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

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


  