import os
import csv

output = os.path.join('.', 'raw_data','election_data_1.csv')
with open(output, newline ='') as results:
    result_reader = csv.reader(results, delimiter = ',')

    #Finding the number of voters 
    next(result_reader)
    result_reader = list(result_reader)
    voter_count = len(result_reader)
    
    #Creating a list of candidates
    cand_list = []
    for i in result_reader:
        if i[2] not in cand_list:
            cand_list.append(i[2])
    
    #Dividing the raw votes by candidate
    cand_vote_1 = 0
    cand_vote_2 = 0
    cand_vote_3 = 0
    cand_vote_4 = 0
    for i in result_reader:
        if i[2] == str(cand_list[0]):
            cand_vote_1 += 1
    for i in result_reader:
        if i[2] == str(cand_list[1]):
            cand_vote_2 += 1
    for i in result_reader:
        if i[2] == str(cand_list[2]):
            cand_vote_3 += 1
    for i in result_reader:
        if i[2] == str(cand_list[3]):
            cand_vote_4 += 1
    
    #Creating a list of the number of votes each candidate received
    cand_vote_list = [cand_vote_1, cand_vote_2, cand_vote_3, cand_vote_4]

    #Finding the percentage of votes each candidate received
    cand_per_1 = (cand_vote_1 / voter_count) * 100
    cand_per_2 = (cand_vote_2 / voter_count) * 100
    cand_per_3 = (cand_vote_3 / voter_count) * 100
    cand_per_4 = (cand_vote_4 / voter_count) * 100

    #Creating a dictionary for reference to find the winner's name
    keys = cand_list
    values = cand_vote_list
    cand_dict = dict(zip(keys,values))
    winner = max(cand_dict, key=cand_dict.get)

    #Printing out in termainal and text
    file = open('Election_results.txt','a')
    print("Election Results") 
    print("-" * 30)
    print("Total Votes: " + str(voter_count))
    print("-" * 30)
    print(cand_list[0] + ": " + str(cand_per_1) + "%" + " (" + str(cand_vote_1) + ")")
    print(cand_list[1] + ": " + str(cand_per_2) + "%" + " (" + str(cand_vote_2) + ")")
    print(cand_list[2] + ": " + str(cand_per_3) + "%" + " (" + str(cand_vote_3) + ")")
    print(cand_list[3] + ": " + str(cand_per_4) + "%" + " (" + str(cand_vote_4) + ")")
    print("-" * 30)
    print("Winner: " + str(winner))
    print("-" * 30)

    file.write("Election Results" + "\n") 
    file.write("-" * 30 + "\n")
    file.write("Total Votes: " + str(voter_count) + "\n")
    file.write("-" * 30 + "\n")
    file.write(cand_list[0] + ": " + str(cand_per_1) + "%" + " (" + str(cand_vote_1) + ")" + "\n")
    file.write(cand_list[1] + ": " + str(cand_per_2) + "%" + " (" + str(cand_vote_2) + ")" + "\n")
    file.write(cand_list[2] + ": " + str(cand_per_3) + "%" + " (" + str(cand_vote_3) + ")" + "\n")
    file.write(cand_list[3] + ": " + str(cand_per_4) + "%" + " (" + str(cand_vote_4) + ")" + "\n")
    file.write("-" * 30 + "\n")
    file.write("Winner: " + str(winner) + "\n")
    file.write("-" * 30 + "\n"
    )