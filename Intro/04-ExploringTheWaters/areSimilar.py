#!/bin/python3
import sys
"""
# Description
# 
# Two arrays are called similar if one can be obtained from another by swapping
# at most one pair of elements in one of the arrays.
#
# Given two arrays a and b, check whether they are similar.
#
# Example:
# 
# For a = [1, 2, 3] and b = [1, 2, 3], the output should be
# areSimilar(a, b) = true.
# 
# The arrays are equal, no need to swap any elements.
# 
# For a = [1, 2, 3] and b = [2, 1, 3], the output should be
# areSimilar(a, b) = true.
# 
# We can obtain b from a by swapping 2 and 1 in b.
# 
# For a = [1, 2, 2] and b = [2, 1, 1], the output should be
# areSimilar(a, b) = false.
# 
# Any swap of any two elements either in a or in b won't make a and b equal.
#
# Input Format
#
# array.integer a
# Array of integers
#
# Constraints
# 3 ≤ a.length ≤ 10**5
# 1 ≤ a[i] ≤ 1000
#
# array.integer b
# Array of integers of the same length as a.
#
# Constraints
# b.length = a.length
# 1 ≤ b[i] ≤ 1000
#
# Output Format 
#
# boolean
# true if a and b are similar, false otherwise.
#
# Solution:
# Solution 1 passes all sample test cases and 3 of 10 hidden test cases. It
# fails on test case 14 for exceeding the time limit.
#
# Solution 2 passes all test cases and simply iterates through each element
# in a and b comparing them and incrementing a counter if they are different.
# If they are different, the elements a[i] and b[i] get added to a set 
# containing the differences diffSet. If the number of differences is <= 2
# and the number of elements in diffSet are <= 2, then the arrays are similar.
"""
##############
# SOLUTION 1 #
##############
#def areSimilar(a, b):
#    if a == b:
#        return True
#    else:
#        for i in range(len(a)-1):
#            tmp = [0] * len(a)
#            for j in range(i+1,len(a)):
#                # Create tmp string to compare against b, which consists of
#                # beg part of list a[0:i], [a[j]] (the first swapped element),
#                # the mid part of list a[i+1:j], [a[i]] (the second swapped
#                # element), and the end of the list a[j+i:]
#                beg = a[0:i]
#                mid = a[i+1:j]
#                end = a[j+1:]
#                tmp = beg + [a[j]] + mid + [a[i]] + end
#                if tmp == b:
#                    return True
#                    break
#        return False
            

##############
# SOLUTION 2 #
##############
def areSimilar(a, b):
    diffs = 0
    diffSet = set()
    for i in range(len(a)):
        if a[i] != b[i]:
            diffs += 1
            diffSet.add(a[i])
            diffSet.add(b[i])
    return True if diffs <= 2 and len(diffSet) <= 2 else False
    
print(areSimilar([1,2,3],[1,2,3]))       # True
print(areSimilar([1,2,3],[2,1,3]))       # True
print(areSimilar([1,2,2],[2,1,1]))       # False
print(areSimilar([2,3,1],[1,3,2]))       # True
print(areSimilar([5,3,2,1],[5,3,1,2]))   # True
print(areSimilar([5,3,2,1],[5,3,7,2]))   # False
print(areSimilar([4,6,3],[3,4,6]))       # False
print(areSimilar([1,1,4],[1,2,3]))       # False
