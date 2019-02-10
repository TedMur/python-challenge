''' ## PyBank
![Revenue](Images/revenue-per-lead.jpg)
* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
* Your task is to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* As an example, your analysis should look similar to the one below:


* In addition, your final script should both print the analysis to the terminal and export a text file with the results.'''

# Modules
import os
import csv


# Set path for file
csvpath = os.path.join("Resources","budget_data.csv")


total_months = 0 
total_amount = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0
great_date = ''
worst_date = ''

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)



    for row in csvreader:
        print(float(row[1]))
        total_months = total_months + 1
        if (greatest_increase < float(row[1])): # Compare values before to find greatest incerase
            great_date = row[0]
            greatest_increase = float(row[1])
        if (greatest_increase > float(row[1])):
            worst_date = row[0]
            greatest_decrease = int(row[1])
        total_amount = total_amount + int(row[1])  #Total revenue
        
        
average_change = total_amount / total_months     

print('Financial Analysis')
print('---------------------------------')
print("Total Months: " + str(total_months))
print("Total: $" + str(total_amount))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits : " + str(great_date) + " $" +str(greatest_increase))
print("Greatest Decrease in Profits : " + str(worst_date) + " $" +str(greatest_decrease))


'''  text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
'''

'''output_path = os.path.join("..", "Output", "PyBank_output")
with open(output_path, "w",newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['---------------------------------'])
    csvwriter.writerow(['Total Months: $' + str(total_months)])
    csvwriter.writerow(['Total: $' + str(total)])
    csvwriter.writerow(['Average Change: ' + str(average_change)])
    csvwriter.writerow(["Greatest Increase in Profits: " + great_date + " $" +str(greatest_increase)])
    csvwriter.writerow(["Greatest Decrease in Profits:" + worst_date + " $" +str(greatest_decrease)])
    csvfile.colse()'''









