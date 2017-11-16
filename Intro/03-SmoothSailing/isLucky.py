#!/bin/python3
import sys
"""
# Description
# 
# Ticket numbers usually consist of an even number of digits. A ticket number 
# is considered lucky if the sum of the first half of the digits is equal to 
# the sum of the second half.
#
# Given a ticket number n, determine if it's lucky or not.
#
# Example:
# 
# For n = 1230, the output should be
# isLucky(n) = true;
#
# For n = 239017, the output should be
# isLucky(n) = false.
#
# Input Format
#
# integer n, A ticket number represented as a positive integer with an even 
# number of digits.
# 10 ≤ n < 10**6
#
# Output Format 
#
# boolean, true if n is a lucky ticket number, false otherwise.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def isLucky(n):
    nStr = str(n)
    firstHalf, secondHalf = 0, 0
    for i in range(len(nStr)//2):
        firstHalf += int(nStr[i])
    for j in range(len(nStr)//2, len(nStr)):
        secondHalf += int(nStr[j])
    return firstHalf == secondHalf

print(isLucky(1234))