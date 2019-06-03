import os

import csv

csvpath = "budget_data.csv"

# Method 2: Improved Reading using CSV module

with open(csvpath, newline='', encoding= 'utf-8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader) # reads the 0 row 
    
    print(f"{csv_header}")

   # for row in csvreader:
    iteration = 0
    count = 0 
    total = 0    
    change = 0
    totalChange = 0   
    prevVal = 0
    currVal = 0
    maxC = 0
    minC = 0
    for row in csvreader:

        month = row[0]
        money = float(row[1])
        total += money
        currVal = money
        

        if iteration == 0:
            prevVal = currVal
        else:
            #currVal = money
            change = currVal - prevVal
            totalChange += change

        if change > maxC:
            maxC = change
            dateMax = row[0]

        if change < minC:
            minC = change
            dateMin = row[0]


        iteration += 1
        prevVal = currVal
            
        if month == month:
            count = count + 1
    
    avgChange = totalChange / (count-1) 


    print(f"Total Months: {count}")  
    print(f"Total: ${total}")
    print (f"Average Change: ${avgChange}")
    print(f"Greatest Increase {dateMax} (${maxC})")
    print(f"Greatest Decrease {dateMin} (${minC})")
    



save = (f"Total Months: {count} Total: ${total} Average Change: ${avgChange} Greatest Increase {dateMax} (${maxC}) Greatest Decrease {dateMin} (${minC})")
    

fileName = input("What do you want your file to be called?") + ".txt"

files = open(fileName, 'w')
files.write(save)
files.close()
os.startfile(fileName)




