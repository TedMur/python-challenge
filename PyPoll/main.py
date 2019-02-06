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

# The total number of votes cast
total_votes = sum(int(electionCSV[0]))


# A complete list of candidates who received votes
    Correy_ = 0
    Khan = 0
    Li = 0
    OTooley = 0
    sum_vote = 0

    for row in csvreader:
        next(csvreader)
        if row[2] == "Correy":
            Correy = Correy + 1
        elif row[2] == "Khan":
            Khan = Khan + 1        
        elif row[2] == "Li":
            Li = Li + 1
        elif row[2] == "O'Tooley":
            OTooley = OTooley + 1
        sum_vote = sum_vote + 1
        
    return
    

        

# The total number of votes cast
total_votes = sum(int(electionCSV[1]))

# A complete list of candidates who received votes


# The percentage of votes each candidate won


# The total number of votes each candidate won    


# The winner of the election based on popular vote.                                                                                             