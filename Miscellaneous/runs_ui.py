#########################################################################################
# Date: December 21, 2021                                                               #
# Author: ShadowRailgun                                                                 #
# Description: User will input numbers which will be appended to a list.                #
#              Program assumes that user will input a number unless they are finished.  #
#              When user is finished they will input q.                                 #
#              At the end of program the length of the longest run of                   #
#              numbers is will be displayed.                                            #
# #######################################################################################

numlist = [] #empty list for input numbers
answer = "" #for the input
while answer != "q": #if they do not input q to exit continue to loop
    answer = input("Add a number or input q to exit: ") #ask for input for answer
    if answer.strip().isdigit(): #if the answer is a number then add it to numlist
        numlist.append(int(answer)) #change input (string) to integer then add it to list
    else: #otherwise strip and change the input to lowercase so that loop only has to check for lowercase
        answer = answer.strip().lower() 
    if len(numlist) == 0: #if list is empty
        answer = "" #reset input to blank so loop will continue
        print("Please input at least one number") #prompt the user that they must input at least one number before quitting
    

numrun = [] #for separate runs
i = 1 #for loop
while i < len(numlist): # loop until end of list
    past = numlist[i-1]
    current = numlist[i]
    checkpast = numlist[i] - 1
    checkcurrent = numlist[i-1] + 1
    # if past and check past are the same and checkpast is not in numrun then append to numrun
    # this is to catch the first number in the run
    if past == checkpast and checkpast not in numrun: 
        numrun.append(checkpast) 
    if current == checkcurrent: # add the next number in the run to the list
        numrun.append(checkcurrent)
    i += 1 # add one to the counter to avoid infinite loop

print(numrun) # print the outcome
i = 1 # reset the counter
l = 1 # this starts as +1 because all numbers in the list are part of a run so the first number [0] does not need to be checked to the previous
runamount = [] # make a new empty list
while i < len(numrun): # loop to end of list of runs
    checkcurrent = numrun[i-1] + 1 
    if numrun[i] == checkcurrent: # if the current number matches the last number then add one to l (length)
        l += 1
        print(i, l, numrun[i]) # to see the count to ensure it is doing it correctly
    else:
        runamount.append(l)
        l = 1 # for first number of the run
    i += 1 # add one to the counter to avoid infinite loop
runamount.append(l) # append length of last run to list
print(runamount) # print list of the lengths of the run

i = 0 # reset counter 
top = 0 # highest number
while i < len(runamount): # loop to end of list of length of runs
    if top < runamount[i]: # if top is a smaller number then the current length being checked then make top the number of the current length
        top = runamount[i]
    i += 1 # add one to the counter to avoid infinite loop

print(top) # print the length of the longest run