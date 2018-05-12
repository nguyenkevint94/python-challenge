import os
import csv

budget = os.path.join('.', 'raw_data', 'budget_data_1.csv')

with open(budget, newline = '') as b1file:
    b1reader = csv.DictReader(b1file)
    total = 0
    #The number of months in each data set
    month_count = sum(1 for months in b1reader)
    #seek(0) starts the loop over again within the with
    b1file.seek(0)
    #Adding dates and corresponding revenue into a list
    b1reader = csv.DictReader(b1file)
    revenues = []
    for summary in b1reader:     
        revenues.append({
            'Date'      : summary["Date"],
            'Revenue'   : int(summary["Revenue"])
        })
        total = total + int(summary["Revenue"])
    b1file.seek(0)
    #Finding and printing the revenue change
    b1list = csv.reader(b1file)
    next(b1list)
    reader_list = list(b1list)
    rev_list = []
    for row in reader_list:
        rev_list.append(int(row[1]))

    avg_list = []
    for i in range(len(rev_list) - 1):
        avg_list.append(rev_list[i]- rev_list[i-1])
    for column in avg_list:
        avg_diff = sum(avg_list) / len(avg_list)

    #finding the greatest increase 
    prev_rev = 0
    greatest_inc = 0
    for summary in revenues:
        if(summary["Revenue"] - prev_rev) > greatest_inc:
            greatest_inc = summary["Revenue"] - prev_rev
            greatest_inc_month = summary["Date"]
        prev_rev = summary["Revenue"]
    #finding the greatesst decrease
    prev_rev = 0
    greatest_dec = 0
    for summary in revenues:
        if(summary["Revenue"] - prev_rev) < greatest_dec:
            greatest_dec = summary["Revenue"] - prev_rev
            greatest_dec_month = summary["Date"]
        prev_rev = summary["Revenue"]

    print("Financial Analysis")
    print("-" * 35)
    print("Total months: " + str(month_count)) 
    print("Total Revenue: $" + str(total))
    print("Average revenue change: $" + str(avg_diff))
    print("Greatest increase in revenue: " + greatest_inc_month + "  $" + str(greatest_inc))
    print("Greatest decrease in revenue: 
    " + greatest_dec_month + "  $" + str(greatest_dec))


    file = open("Financial_Analysis.txt","a")
    file.write("Financial Analysis" + "\n")
    file.write("-" * 35 + "\n")
    file.write("Total months: " + str(month_count) + "\n")
    file.write("Total Revenue: $" + str(total) + "\n")
    file.write("Average revenue change: $" + str(avg_diff) + "\n")
    file.write("Greatest decrease in revenue: " + greatest_inc_month + "  $" + str(greatest_inc) + "\n")
    file.write("Greatest decrease in revenue: " + greatest_dec_month + "  $" + str(greatest_dec) + "\n")