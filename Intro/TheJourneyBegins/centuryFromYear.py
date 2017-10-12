#!/bin/python3
import sys
"""
# Description
# Difficulty: Easy
# 
# Given a year, return the century it is in. The first century spans from the 
# year 1 up to and including the year 100, the second - from the year 101 up 
# to and including the year 200, etc..
#
# Example:
# 
# For year = 1905, the output should be
# centuryFromYear(year) = 20;
#
# For year = 1700, the output should be
# centuryFromYear(year) = 17.
#
# Input Format
#
# Integer year, A positive integer, designating the year.
# 1 <= year <= 2005
#
# Output Format 
#
# The number of the century the year is in.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def centuryFromYear(year):
    cent = year // 100
    if year % 100 != 0:
        cent += 1
    return cent