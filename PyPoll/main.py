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
        
        # The percentage of votes each candidate won
        Khan_percentage = round((Khan / sum_vote)*100, 3)
        Correy_percentage = round((Correy / sum_vote)*100, 3)
        Li_percentage = round((Li / sum_vote)*100, 3)
        OTooley_percentage = round((OTooley / sum_vote)*100, 3)

        
        # The winner of the election based on popular vote.  
        candidates_dict = {"Correy": int(Correy), "Khan": int(Khan), "Li": int(Li), "O'Tooley": int(OTooley)}
        winner = max(candidates_dict, key=candidates_dict.get)
        

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {sum_vote}")
    print("-------------------------")
    print(f"Khan: {Khan_percentage}% ({Khan})")
    print(f"Correy: {Correy_percentage}% ({Correy})")
    print(f"Li: {Li_percentage}% ({Li})")
    print(f"O'Tooley:  {OTooley_percentage}% ({OTooley})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")
        


output_path = os.path.join("Output", "PyPoll_output") 
with open(output_path, 'w', newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Total Votes: {sum_vote}"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Khan: {Khan_percentage}% ({Khan})"])
    csvwriter.writerow([f"Correy: {Correy_percentage}% ({Correy})"])
    csvwriter.writerow([f"Li: {Li_percentage}% ({Li})"])
    csvwriter.writerow([f"O'Tooley:  {OTooley_percentage}% ({OTooley})"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["-------------------------"])
