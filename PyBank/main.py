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
num = 0
pl_list = []
new = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    for row in csvreader:

        total_months = total_months + 1
        if (greatest_increase < float(row[1])): # Compare values before to find greatest incerase
            great_date = row[0]
            greatest_increase = float(row[1])
        if (greatest_increase > float(row[1])):
            worst_date = row[0]
            greatest_decrease = int(row[1])
        total_amount = total_amount + int(row[1])  #Total revenue
        pl_list.append(row[1])


        average_change = round((total_amount / total_months), 2) #Incorrect function

'''for x in pl_list:
    #keep num <= to 84 to stay in list range
    if num <= 84:
        #check change by month and add to average_change
        check =  - int(pl_list[num]) + int(pl_list[(num+1)])
        average_change += check
        num += 1 
        #append averages by month to list
        new.append(check)


#round to two decimals
average_round = round((average_change/num), 2)
# average_change = total_amount / total_months  '''   

print('Financial Analysis')
print('---------------------------------')
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${average_change}") # Not correct
print(f"Greatest Increase in Profits : {great_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits : {worst_date} (${greatest_decrease})")


'''output_path = os.path.join("Output", "PyBank_output")
with open(output_path, "w",newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['---------------------------------'])
    csvwriter.writerow([f"Total Months: {total_months}"])
    csvwriter.writerow([f"Total: ${total_amount}"])
    csvwriter.writerow([f"Average Change: ${average_change}"])
    csvwriter.writerow([f"Greatest Increase in Profits : {great_date} (${greatest_increase})"])
    csvwriter.writerow([f"Greatest Decrease in Profits : {worst_date} (${greatest_decrease})"])
    csvfile.close()'''









