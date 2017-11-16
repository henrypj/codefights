#!/bin/python3
import sys
"""
# Description
# 
# Given a sequence of integers as an array, determine whether it is possible to
# obtain a strictly increasing sequence by removing no more than one element 
# from the array.
#
# Example:
# 
# For sequence = [1, 3, 2, 1], the output should be
# almostIncreasingSequence(sequence) = false;
#
# There is no one element in this array that can be removed in order to get a 
# strictly increasing sequence.
#
# For sequence = [1, 3, 2], the output should be
# almostIncreasingSequence(sequence) = true.
#
# You can remove 3 from the array to get the strictly increasing sequence 
# [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence
# [1, 3].
#
# Input Format
#
# array.integer sequence
# 2 ≤ sequence.length ≤ 10**5
# -10**5 ≤ sequence[i] ≤ 10**5
#
# Output Format 
#
# Return true if it is possible to remove one element from the array in order 
# to get a strictly increasing sequence, otherwise return false.
#
# Solution:
# Solution 1 involves using numpy, but when attempting to use it in
# codefights, it says that numpy module cannot be found.
#
# Solution 2 and 3 does not use numpy and passes 32 of 34 test cases, but times
# out on test case 33. According to comments, this test case has 1000's of items
# so creating a new list with each iteration is probably causing the timeout.
#
# Solution 4 simply goes through the list of integers one time making 
# comparisons to ensure that it is increasing, and increasing a failure 
# counter for cases where it does not. This passes all test cases.
#
# Solution 5 is not my solution, but was in the comments. It is close to my
# solution 4, but less code and a bit more elegant.
"""
##############
# SOLUTION 1 #
##############
#import numpy as np
#
#def monotonic(x):
#    dx = np.diff(x)
#    return np.all(dx >= 0)
##    return np.all(dx <= 0) or np.all(dx >= 0)
#
#def almostIncreasingSequence(sequence):
#    for i in range(len(sequence)):
#        tmp = list(sequence)
#        tmp.pop(i)
#        if monotonic(tmp) == True:
#            return True
#    return False
#    
#print(almostIncreasingSequence([1,3,2,1]))    
#print(almostIncreasingSequence([1,3,2]))    
    

##############
# SOLUTION 2 #
##############
#def strictly_increasing(L):
#    return all(x<y for x, y in zip(L, L[1:]))
#
#def almostIncreasingSequence(sequence):
#    for i in range(len(sequence)):
#        tmp = list(sequence)
#        tmp.pop(i)
#        if strictly_increasing(tmp) == True:
#            return True
#    return False
#    
#print(almostIncreasingSequence([1,3,2,1]))    
#print(almostIncreasingSequence([1,3,2]))    
    

##############
# SOLUTION 3 #
##############
#def strictly_increasing(L):
#    for j in range(len(L)-1):
#        if L[j+1] <= L[j]:
#            return False
#    return True
#        
#def almostIncreasingSequence(sequence):
#    for i in range(len(sequence)):
#        tmp = list(sequence)
#        tmp.pop(i)
#        if strictly_increasing(tmp) == True:
#            return True
#    return False
#    
#print(almostIncreasingSequence([1,3,2,1]))    
#print(almostIncreasingSequence([1,3,2]))    
    

##############
# SOLUTION 4 #
##############
def almostIncreasingSequence(sequence):    
    numFail = 0
    prev = sequence[0]
    for i in range(len(sequence)-1):
        if sequence[i+1] <= prev:
            numFail += 1
            if i == 0:
                prev = sequence[i+1] 
            elif i <= len(sequence)-3 and sequence[i+2] <= sequence[i]:
                if sequence[i+1] > sequence[i-1]:
                    prev = sequence[i+1]
                else:
                    prev = sequence[i]
                if sequence[i+2] <= prev:
                    numFail += 1
            else:
                prev = sequence[i]
            if numFail > 1:
                return False
        else:
            prev = sequence[i+1]

    return True

##############
# SOLUTION 5 #
##############
#def almostIncreasingSequence(sequence):    
#    count_decreasing_sq = 0
#    for i in range(len(sequence) - 1):
#        if sequence[i+1] <= sequence[i]:
#            count_decreasing_sq += 1
#            if (i >= 1) and (sequence[i+1] <= sequence[i-1]):
#                if (len(sequence) - 2 > i) and (sequence[i+2] <= sequence[i]):
#                    count_decreasing_sq += 1
#        if count_decreasing_sq > 1:
#            return False
#    
#    return True



    
print(almostIncreasingSequence([1,3,2,1]))         # False
print(almostIncreasingSequence([1,3,2]))           # True
print(almostIncreasingSequence([2,3,1,3]))         # False
print(almostIncreasingSequence([1,3,1,2]))         # False
print(almostIncreasingSequence([10,1,2,3,4,5]))    # True
print(almostIncreasingSequence([1,2,3,4,5,6]))     # True
print(almostIncreasingSequence([3,5,3,6]))         # True
print(almostIncreasingSequence([1,2,5,3,4,5]))     # True
print(almostIncreasingSequence([1,2,5,5,5]))       # False