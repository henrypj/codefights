#!/bin/python3
import sys
"""
# Description
# 
# Let's define digit degree of some positive integer as the number of times we 
# need to replace this number with the sum of its digits until we get to a one 
# digit number.
#
# Given an integer, find its digit degree.
# 
# Example
#
# For n = 5, the output should be
# digitDegree(n) = 0;
#
# For n = 100, the output should be
# digitDegree(n) = 1.
# 1 + 0 + 0 = 1.
#
# For n = 91, the output should be
# digitDegree(n) = 2.
# 9 + 1 = 10 -> 1 + 0 = 1.
#
# Input/Output
#
# [input] integer n
# Guaranteed constraints:
# 5 ≤ n ≤ 10**9.
#
# [output] integer
#
# Solution:
#
"""
##############
# SOLUTION 1 #
##############
#def digitDegree(n):
#    cnt = 0
#    sum = 0
#    if len(str(n)) == 1:
#        return 0
#        
#    for digit in str(n):
#        sum += int(digit)
#
#    if sum // 10 <= 0:
#        return cnt+1
#    else:
#        while sum // 10 > 0:
#            newSum = sum
#            sum = 0
#            for digit in str(newSum):
#                sum += int(digit)
#                cnt += 1
#    return cnt

##############
# SOLUTION 2 #
##############
def digitDegree(n):
    count = 0
    while n > 9:
        count += 1
        n = sum(int(i) for i in str(n))
    return count
	
print(digitDegree(5))	                             # 0
print(digitDegree(1001))	                             # 1
print(digitDegree(91))	                             # 2
print(digitDegree(99))	                             # 2
print(digitDegree(1))	                             # 2
