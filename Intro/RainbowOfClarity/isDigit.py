#!/bin/python3
import sys
"""
# Description
# 
# Determine if the given character is a digit or not.
#
# Example
#
# For symbol = '0', the output should be
# isDigit(symbol) = true;
#
# For symbol = '-', the output should be
# isDigit(symbol) = false.
#
# Input/Output
#
# [input] char symbol
# A character which is either a digit or not.
# 
# [output] boolean
# true if symbol is a digit, false otherwise.
#
# Solution:
# This is a trivial problem in Python as there is an isdigit method that can
# be used, as I did in Solution 1. Solution 2 is a method that does not utilize
# the built in isdigit method.
"""
##############
# SOLUTION 1 #
##############
def isDigit(symbol):
    return symbol.isdigit()

##############
# SOLUTION 2 #
##############
#def isDigit(symbol):
#    digits = "0123456789"
#    return True if symbol in digits else False


print(isDigit('0'))                 # True
print(isDigit('-'))                 # False
print(isDigit('O'))                 # False
print(isDigit('1'))                 # True
print(isDigit('2'))                 # True
print(isDigit('!'))                 # False
print(isDigit('@'))                 # False
print(isDigit('+'))                 # False
print(isDigit('6'))                 # True
print(isDigit('('))                 # False

