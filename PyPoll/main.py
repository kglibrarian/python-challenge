# Import the os module to create file paths across operating systems
import os

# Import the csv module for reading CSV files
import csv

csvpath = os.path.join('election_data_test.csv')

def voterInfo(voterID, county, candidate):
    print("Election Results")

    #The total number of votes cast
    voterSum = len(voterID)
    print(f"Total Votes: {voterSum}")
   
    #A complete list of candidates who received votes
    #candidateUnique = set(candidate)
    #print(candidateUnique)

    #Create dicitonary of Key: candidate name and Value: number of votes
    candidateSum = {i:candidate.count(i) for i in candidate}
    
    #print("candidateSum: ", candidateSum)
    winner = max(candidateSum, key=candidateSum.get)  
    #print("Winner: ", winner, candidateSum[winner])
    


    #create an empty dictionary for the final data
    finalData = {}

    #loop through each Key: candidate in our current dictionary
    for i in candidateSum: 
        
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
    
    test = []
    #loop through the items in the dictionary and print them
    for k, v in finalData.items():
        #print(k, v[0], v[1])
        print(f"{k}: {v[0]} ({v[1]})")
        #the code below is just to get access to print this outside of the loop
        name = k
        percent = v[0]
        votes = v[1]
        test.append(name)
        test.append(percent)
        test.append(votes)
        
    #print(test)
        
    
    
    #dictionary comprehension version
    #test = {k:v for k, v in finalData.items()}
    #print("test is: " , test)
    
    winner = max(finalData, key=finalData.get)  
    print("Winner: ", winner)
    
    f = open("results.txt", 'w')
    f.write("Election Results\n" f"Total Votes: {voterSum}\n"  f"{test[0]}  {test[1]}  ({test[2]})\n" f"Winner: {winner}\n")
    f.close()

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


  