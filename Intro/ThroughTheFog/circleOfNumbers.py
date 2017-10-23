#!/bin/python3
import sys
"""
# Description
# 
# Consider integer numbers from 0 to n - 1 written down along the circle in 
# such a way that the distance between any two neighbouring numbers is equal 
# (note that 0 and n - 1 are neighbouring, too).
#
# Given n and firstNumber, find the number which is written in the radially 
# opposite position to firstNumber.
#
# Example:
# 
# For n = 10 and firstNumber = 2, the output should be
# circleOfNumbers(n, firstNumber) = 7.
#
# Input Format
#
# integer n
# A positive even integer
# 4 ≤ n ≤ 20.
#
# # integer firstNumber
# 0 ≤ firstNumber ≤ n - 1.
#
# Output Format
#
# integer
#
# Solution:
# 
"""
##############
# SOLUTION 1 #
##############
def circleOfNumbers(n, firstNumber):
    return firstNumber - n // 2 if firstNumber >= n // 2 else firstNumber + n // 2

print(circleOfNumbers(10,2))            # 7
print(circleOfNumbers(10,7))            # 2
print(circleOfNumbers(4,1))             # 3
print(circleOfNumbers(6,3))             # 0
