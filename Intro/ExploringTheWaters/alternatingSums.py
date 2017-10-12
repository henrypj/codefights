#!/bin/python3
import sys
"""
# Description
# 
# Several people are standing in a row and need to be divided into two teams. 
# The first person goes into team 1, the second goes into team 2, the third 
# goes into team 1 again, the fourth into team 2, and so on.
#
# You are given an array of positive integers - the weights of the people. 
# Return an array of two integers, where the first element is the total weight
# of team 1, and the second element is the total weight of team 2 after the 
# division is complete.
#
# Example:
# 
# For a = [50, 60, 60, 45, 70], the output should be
# alternatingSums(a) = [180, 105].
#
# Input Format
#
# array.integer a
#
# Constraints
# 1 ≤ a.length ≤ 10,
# 45 ≤ a[i] ≤ 100.
#
# Output Format 
#
# array.integer
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def alternatingSums(a):
    sumList = []
    team1 = sum(num for num in a[0::2])
    team2 = sum(num for num in a[1::2])
    sumList.append(team1)
    sumList.append(team2)
    return(sumList)
    
a = [50, 60, 60, 45, 70]
print(alternatingSums(a))    