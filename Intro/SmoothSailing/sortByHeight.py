#!/bin/python3
import sys
"""
# Description
# 
# Some people are standing in a row in a park. There are trees between them 
# which cannot be moved. Your task is to rearrange the people by their heights
# in a non-descending order without moving the trees.
#
# Example:
# 
# For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
# sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
#
# Input Format
#
# array.integer a
# If a[i] = -1, then the ith position is occupied by a tree. Otherwise a[i] is
# the height of a person standing in the ith position.
# 5 ≤ a.length ≤ 15
# -1 ≤ a[i] ≤ 200
#
# Output Format 
#
# array.integer Sorted array a with all the trees untouched.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def sortByHeight(a):
    j = 0
    heights = []
    people = sorted(i for i in a if i >= 0)
    for i in range(len(a)):
        if a[i] == -1:
            heights.append(a[i]) 
        else:
            heights.append(people[j])
            j += 1
    return heights
    
a = [-1, 150, 190, 170, -1, -1, 160, 180]
print(sortByHeight(a))