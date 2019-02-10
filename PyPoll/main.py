'''* In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example, your analysis should look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------'''


# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    '''row_count = sum(1 for row in csvreader)
    print(row_count)'''

    Correy = 0
    Khan = 0
    Li = 0
    OTooley = 0
    sum_vote = 0

    for row in csvreader:
        next(csvreader)

        # A complete list of candidates who received votes and
        # The total number of votes each candidate won
        if row[2] == "Correy":
            Correy = Correy + 1
        elif row[2] == "Khan":
            Khan = Khan + 1        
        elif row[2] == "Li":
            Li = Li + 1
        elif row[2] == "O'Tooley":
            OTooley = OTooley + 1
        
        # The total number of votes cast
        
        sum_vote = sum_vote + 1
        
        '''# The percentage of votes each candidate won
        Khan_percentage = round((Khan / sum_vote)*100, 3)
        Correy_percentage = round((Correy / sum_vote)*100, 3)
        Li_percentage = round((Li / sum_vote)*100, 3)
        OTooley_percentage = round((OTooley / sum_vote)*100, 3)'''

        
        # The winner of the election based on popular vote.  
        candidates_dict = [Correy, Khan, Li, OTooley]
        winner = max(candidates_dict)
        

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {sum_vote}")
    print("-------------------------")
    '''
    print(f"Khan: {Khan_percentage}% ({Khan})")
    print(f"Correy: {Correy_percentage}% ({Correy})")
    print(f"Li: {Li_percentage}% ({Li})")
    print(f"O'Tooley:  {OTooley_percentage}% ({OTooley})")
    '''
    print("-------------------------")
    print("Winner: {winner}")
    print("-------------------------")
        


'''output_path = os.path.join("Output", "PyPoll_output") 
with open(output_path, 'w', newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow(["Total Votes: ", sum_vote])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow(["Khan: "])
    csvwriter.writerow(["Correy: "])
    csvwriter.writerow(["Li: "])
    csvwriter.writerow(["O'Tooley: "])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow(["Winner: "])
'''
