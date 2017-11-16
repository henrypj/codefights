#!/bin/python3
import sys
"""
# Description
# 
# You found two items in a treasure chest! The first item weighs weight1 and 
# is worth value1, and the second item weighs weight2 and is worth value2. 
# What is the total maximum value of the items you can take with you, assuming 
# that your max weight capacity is maxW and you can't come back for the items 
# later?
# 
# Note that there are only two items and you can't bring more than one item of 
# each type, i.e. you can't take two first items or two second items.
#
# Example:
# 
# For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4 and maxW = 8, the 
# output should be
# knapsackLight(value1, weight1, value2, weight2, maxW) = 10.
# 
# You can only carry the first item.
# 
# For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4 and maxW = 9, the 
# output should be
# knapsackLight(value1, weight1, value2, weight2, maxW) = 16.
#
# You're strong enough to take both of the items with you.
#
# For value1 = 5, weight1 = 3, value2 = 7, weight2 = 4 and maxW = 6, the 
# output should be
# knapsackLight(value1, weight1, value2, weight2, maxW) = 7.
#
# You can't take both items, but you can take any of them.
#
# Input/Output
#
# [input] integer value1
# Guaranteed constraints:
# 2 ≤ value1 ≤ 20.
#
# [input] integer weight1
# Guaranteed constraints:
# 2 ≤ weight1 ≤ 10.
#
# [input] integer value2
# Guaranteed constraints:
# 2 ≤ value2 ≤ 20.
#
# [input] integer weight2
# Guaranteed constraints:
# 2 ≤ weight2 ≤ 10.
#
# [input] integer maxW
# Guaranteed constraints:
# 1 ≤ maxW ≤ 20.
#
# [output] integer
#
# Solution:
# Solution 1 is functionally correct and passed all sample test cases, but 
# failed on first hidden test case due to timeout. 
# There was a bug in my original solution where I did not account for the 
# case where both items are used, but the total weight is still < maxW. I
# had to add a check at the end of the while loop to check if both items
# were used and if so, set maxedOut to True. The solution is more complicated
# than it needs to be, however. Solution2 is a much more simplified version.
#
"""
##############
# SOLUTION 1 #
##############
#def knapsackLight(value1, weight1, value2, weight2, maxW):
#    totalWt  = 0
#    totalVal = 0
#    item1Used = False
#    item2Used = False
#    maxedOut = True if min(weight1, weight2) > maxW else False
#
#    while totalWt < maxW and not maxedOut:
#        if value1 == value2:
#            if weight1 <= weight2 and totalWt + weight1 <= maxW and not item1Used:
#                totalWt  += weight1
#                totalVal += value1
#                item1Used = True
#            elif totalWt + weight2 <= maxW and not item2Used:
#                totalWt  += weight2
#                totalVal += value2
#                item2Used = True
#        elif value1 > value2:
#            if totalWt + weight1 <= maxW and not item1Used:
#                totalWt  += weight1
#                totalVal += value1
#                item1Used = True
#            elif totalWt + weight2 <= maxW and not item2Used:
#                totalWt  += weight2
#                totalVal += value2
#                item2Used = True
#        else:
#            if totalWt + weight2 <= maxW and not item2Used:
#                totalWt  += weight2
#                totalVal += value2
#                item2Used = True
#            elif totalWt + weight1 <= maxW and not item1Used:
#                totalWt  += weight1
#                totalVal += value1
#                item1Used = True
#
#        if item1Used and item2Used:
#            maxedOut = True
#        elif item1Used:
#            if totalWt + weight2 > maxW:
#                maxedOut = True
#        elif item2Used:
#            if totalWt + weight1 > maxW:
#                maxedOut = True
#    return totalVal

##############
# SOLUTION 2 #
##############
def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    if weight1 <= maxW and (value1 > value2 or weight2 > maxW):
        return value1
    if weight2 <= maxW:
        return value2
    return 0


	
print(knapsackLight(10, 5, 6, 4, 8))				# 10
print(knapsackLight(10, 5, 6, 4, 9))				# 16
print(knapsackLight(5, 3, 7, 4, 6))				# 7
print(knapsackLight(10, 2, 11, 3, 1))				# 0
print(knapsackLight(15, 2, 20, 3, 2))				# 15
print(knapsackLight(2, 5, 3, 4, 5))				# 3
print(knapsackLight(4, 3, 3, 4, 4))				# 4
print(knapsackLight(3, 5, 3, 8, 10))				# 3
print(knapsackLight(3, 4, 5, 3, 3))				# 5
print(knapsackLight(5, 2, 4, 2, 20))				# 9
print(knapsackLight(2, 2, 2, 2, 2))				# 2
print(knapsackLight(10, 4, 11, 5, 3))				# 0
print(knapsackLight(10, 4, 11, 5, 6))				# 11
print(knapsackLight(4, 5, 6, 5, 4))				# 0
