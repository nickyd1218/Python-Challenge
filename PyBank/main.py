import os
import csv

myFile = os.path.join("Resources/budget_data.csv")

month_count = 0
P_L = 0
Max = 0
Min = 0
data =[]
data2=[]

#Initialize
with open(myFile, newline="") as csvfile:
    csvreader= csv.reader(csvfile,delimiter=",")
    
#Start looking at rows AFTER the first row (header)
    next(csvreader)
    
#Sum up the total amount of months
    for row in csvreader:    
        if row[0] == "Jan" or "Feb" or "Mar" or "Apr" or "May" or "Jun" or "Jul" or "Aug" or "Sep" or "Oct" or "Nov" or "Dec":
            month_count = month_count + 1

#Sum up totals for revenue
            P_L += int(row[1])
 #           P_L += float(row[1])

#Convert column 1 into an array
            data.append(row[1])

#Convert column 0 into an array
#(to index locate the corresponding months at end)
            data2.append(row[0])
            
#Calculate average (rounded to 2 points after decimal)         
avgChg = round(int(P_L)/int(month_count),2)

#Find max
Max = max(data)
#Find min
Min = min(data)

#Find the Max and Min indices 
x = data.index(Max)
y = data.index(Min)

#Find the correspond month/year to the Max and Min via index lookup
maxMon = data2[x]
minMon = data2[y]

#Output everything to terminal

print("                                         ")
print("Financial Analysis")
print("------------------------")
print("Total Months: " + str(month_count))
print("Total: $" + str(P_L))
print("Average Change: $" + str(avgChg))
print("Greatest Increase in Profits : " + maxMon + "  ($" + str(Max) + ")")
print("Greatest Decrease in Profits : " + minMon + "  ($" + str(Min) + ")")
print("                                         ")
#print(max(data))
#print(min(data))

#Export Text file
output_path = os.path.join("Resources/PyBank.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['--------------------------'])
    csvwriter.writerow(['Total Months: ' + str(month_count)])
    csvwriter.writerow(['Total: $' + str(P_L)])
    csvwriter.writerow(['Average Change: $' + str(avgChg)])
    csvwriter.writerow(['Greatest Increase in Profits : ' + maxMon + '  ($' + str(Max) + ')'])
    csvwriter.writerow(['Greatest Decrease in Profits : ' + minMon + '  ($' + str(Min) + ')'])


