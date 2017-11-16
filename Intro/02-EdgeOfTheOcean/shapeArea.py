#!/bin/python3
import sys
"""
# Description
# 
# Below we will define an n-interesting polygon. Your task is to find the area
# of a polygon for a given n.
#
# A 1-interesting polygon is just a square with a side of length 1. An 
# n-interesting polygon is obtained by taking the n - 1-interesting polygon 
# and appending 1-interesting polygons to its rim, side by side. You can see
# the 1-, 2-, 3- and 4-interesting polygons in the picture below.
#
#    |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
# ---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
#    |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
# ---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
#    |   |   |   |   |   |   |   |   | X |   |   |   |   |   | X | X | X |   |
# ---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
#    |   |   |   | X |   |   |   | X | X | X |   |   |   | X | X | X | X | X |
# ---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
#    | X |   | X | X | X |   | X | X | X | X | X |   | X | X | X | X | X | X | X
# ---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
#    |   |   |   | X |   |   |   | X | X | X |   |   |   | X | X | X | X | X |
# ---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
#    |   |   |   |   |   |   |   |   | X |   |   |   |   |   | X | X | X |   |
# ---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
#    |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |
# ---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
#    |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
#
#     n=1         n=2                 n=3                         n=4
#
# Example:
# 
# For n = 2, the output should be
# shapeArea(n) = 5    
#
# For n = 3, the output should be
# shapeArea(n) = 13   
#
# For n = 4, the output should be
# shapeArea(n) = 25   
#
# For n = 5, the output should be
# shapeArea(n) = 41
#
# Input Format
#
# integer n
# 1 ≤ n < 10**4
#
# Output Format 
#
# The area of the n-interesting polygon.
#
# Solution:
# For solution 1 I used recursion, but given how large n can be, it would 
# fail on large numbers of n.
#
# For solution 2, I used the pattern that shapeArea = n**2 + (n-1)**2
"""
##############
# SOLUTION 1 #
##############
#def shapeArea(n):
#    return 1 if n ==1 else (shapeArea(n-1) + ((n-1) * 4))
#
#print(shapeArea(1))
#print(shapeArea(2))
#print(shapeArea(3))
#print(shapeArea(4))
#print(shapeArea(10000))

##############
# SOLUTION 2 #
##############
def shapeArea(n):
    return (n**2 + ((n-1)**2))

print(shapeArea(1))
print(shapeArea(2))
print(shapeArea(3))
print(shapeArea(4))
print(shapeArea(10000))