##################################################################################
# Date: December 19, 2021                                                        #
# Author: ShadowRailgun                                                          #
# Description: From the hardcoded list of numbers find what the                  #
#              length of the longest run of numbers is and display it at the end #
# ################################################################################

numlist = [42, 100, 10, 5, 6, 7, 53, 9, 10, 11, 12] #hardcoded numbers
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