#!/bin/python3
import sys
"""
# Description
# 
# Call two arms equally strong if the heaviest weights they each are able to 
# lift are equal.
#
# Call two people equally strong if their strongest arms are equally strong 
# (the strongest arm can be both the right and the left), and so are their 
# weakest arms.
#
# Given your and your friend's arms' lifting capabilities find out if you two 
# are equally strong.
#
# Example:
# 
# For yourLeft = 10, yourRight = 15, friendsLeft = 15 and friendsRight = 10, 
# the output should be
# areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
#
# For yourLeft = 15, yourRight = 10, friendsLeft = 15 and friendsRight = 10, 
# the output should be
# areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
#
# For yourLeft = 15, yourRight = 10, friendsLeft = 15 and friendsRight = 9, 
# the output should be
# areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = false.
#
# Input Format
#
# integer yourLeft
# A non-negative integer representing the heaviest weight you can lift with 
# your left arm.
#
# Constraints
# 0 ≤ yourLeft ≤ 20
#
# integer yourRight
# A non-negative integer representing the heaviest weight you can lift with 
# your right arm.
#
# Constraints
# 0 ≤ yourLeft ≤ 20
#
# integer friendsLeft
# A non-negative integer representing the heaviest weight your friend can lift 
# with his or her left arm.
#
# Constraints
# 0 ≤ yourLeft ≤ 20
#
# integer friendsRight
# A non-negative integer representing the heaviest weight your friend can lift 
# with his or her Right arm.
#
# Constraints
# 0 ≤ yourLeft ≤ 20
#
# Output Format 
#
# boolean
# true if you and your friend are equally strong, false otherwise.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    myStrongest      = max(yourLeft, yourRight)
    myWeakest        = min(yourLeft, yourRight)
    friendsStrongest = max(friendsLeft, friendsRight)
    friendsWeakest   = min(friendsLeft, friendsRight)
    return True if (myStrongest == friendsStrongest and
                    myWeakest   == friendsWeakest) else False
    
    
print(areEquallyStrong(10,15,15,10))        # True
print(areEquallyStrong(15,10,15,10))        # True    
print(areEquallyStrong(15,10,15,9))         # False
print(areEquallyStrong(10,5,5,10))          # True
print(areEquallyStrong(10,15,5,20))         # False
print(areEquallyStrong(5,20,20,5))          # True
print(areEquallyStrong(20,15,5,20))         # False
print(areEquallyStrong(5,10,5,10))          # True
print(areEquallyStrong(1,10,10,0))          # False
print(areEquallyStrong(5,5,10,10))          # False
print(areEquallyStrong(1,1,1,1))            # True    