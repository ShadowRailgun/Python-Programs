#########################################################################################
# Date: December 21, 2021                                                               #
# Author: ShadowRailgun                                                                 #
# Description: User will input a radian which will be converted to degrees.             #
# #######################################################################################

import math #import math for the pi function

radian = input("Input a radian: ") #ask user to input a radian
degrees = int(radian) * (180 / math.pi) #calculation for degrees from radian
print(round(degrees, 4)) #print output rounded to 4 decimal points