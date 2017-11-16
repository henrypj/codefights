#!/bin/python3
import sys
"""
# Description
# 
# Check if all digits of the given integer are even.
#
# Example:
# 
# For n = 248622, the output should be
# evenDigitsOnly(n) = true;
#
# For n = 642386, the output should be
# evenDigitsOnly(n) = false..
#
# Input Format
#
# integer n
#
# Constraints
# 1 ≤ n ≤ 10**9
#
# Output Format
#
# boolean
# true if all digits of n are even, false otherwise.
#
# Solution:
# 
"""
##############
# SOLUTION 1 #
##############
#def evenDigitsOnly(n):
#    digits = [int(d) for d in str(n)]
#    for i in range(len(digits)):
#        if digits[i] % 2 != 0:
#            return False
#    return True


##############
# SOLUTION 2 #
##############
def evenDigitsOnly(n):
    return all([int(x) % 2 == 0 for x in list(str(n))])

print(evenDigitsOnly(248622))                   # True
print(evenDigitsOnly(642386))                   # False
print(evenDigitsOnly(248842))                   # True
print(evenDigitsOnly(1))                        # False
print(evenDigitsOnly(8))                        # True
print(evenDigitsOnly(2462487))                  # False
print(evenDigitsOnly(468402800))                # True
print(evenDigitsOnly(2468428))                  # True
print(evenDigitsOnly(5468428))                  # False
print(evenDigitsOnly(7468428))                  # False
